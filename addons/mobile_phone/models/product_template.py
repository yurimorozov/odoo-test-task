# -*- coding: utf-8 -*-
from odoo import fields, models, api, exceptions


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    manufacturer_id = fields.Many2one('mobile.phone.manufacturer', ondelete='set null', string="Manufacturer")
    model_id = fields.Many2one('mobile.phone.model', ondelete='set null', string="Model",
                               domain="[('manufacturer_id', '=', manufacturer_id)]")

    @api.onchange('manufacturer_id')
    def _verify_model(self):
        if self.manufacturer_id != self.model_id.manufacturer_id:
            self.model_id = None

    @api.constrains('manufacturer_id', 'model_id')
    def _check_model(self):
        for product in self:
            if product.manufacturer_id and not product.model_id:
                raise exceptions.ValidationError("Select model of mobile phone")

