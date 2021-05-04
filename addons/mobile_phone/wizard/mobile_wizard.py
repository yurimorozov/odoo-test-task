# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, exceptions, _


class MobileWizard(models.TransientModel):
    _name = 'mobile.phone.wizard'
    _description = "Wizard: Quick product creating"

    @tools.ormcache()
    def _get_default_category_id(self):
        # Deletion forbidden (at least through unlink)
        return self.env.ref('product.product_category_all')

    name = fields.Char('Product Name', compute='_compute_name')
    type = fields.Selection([('consu', 'Consumable'),
                             ('service', 'Service')], string='Product Type', default='consu')
    categ_id = fields.Many2one('product.category', 'Product Category', default=_get_default_category_id)
    sale_ok = fields.Boolean('Can be Sold', default=True)
    purchase_ok = fields.Boolean('Can be Purchased', default=True)
    default_code = fields.Char('Internal Reference')
    manufacturer_id = fields.Many2one('mobile.phone.manufacturer', ondelete='set null', string="Manufacturer")
    model_id = fields.Many2one('mobile.phone.model', ondelete='set null', string="Model",
                               domain="[('manufacturer_id', '=', manufacturer_id)]")
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    state = fields.Selection(selection=[('step1', 'Step 1'),
                                        ('step2', 'Step 2')], default="step1", readonly=True)

    @api.onchange('manufacturer_id')
    def _verify_model(self):
        if self.manufacturer_id != self.model_id.manufacturer_id:
            self.model_id = None

    @api.depends('manufacturer_id', 'model_id')
    def _compute_name(self):
        self.name = ''

        if self.manufacturer_id:
            self.name = self.manufacturer_id.name

        if self.model_id:
            self.name += ' ' + self.model_id.name

    def action_step1(self):
        self.state = 'step1'
        return {
            'context': self.env.context,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mobile.phone.wizard',
            'res_id': self.id,
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    def action_step2(self):
        if not self.manufacturer_id or not self.model_id:
            raise exceptions.ValidationError("Select model of mobile phone")

        self.state = 'step2'
        return {
            'context': self.env.context,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mobile.phone.wizard',
            'res_id': self.id,
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    def save_product(self):
        new_product = {
           'name': self.name,
           'type': self.type,
           'categ_id': self.categ_id.id,
           'sale_ok': self.sale_ok,
           'purchase_ok': self.purchase_ok,
           'default_code': self.default_code,
           'manufacturer_id': self.manufacturer_id.id,
           'model_id': self.model_id.id,
           'image_1920': self.image_1920,
        }

        self.env['product.template'].create(new_product)
