# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class Manufacturer(models.Model):
    _name = 'mobile.phone.manufacturer'
    _description = "Mobile phone manufacturer"

    name = fields.Char(string="Name", required=True)

    phone_model_ids = fields.One2many('mobile.phone.model', 'manufacturer_id', string="Models", readonly=True)


class PhoneModel(models.Model):
    _name = 'mobile.phone.model'
    _description = "Model of mobile phone"

    name = fields.Char(string="Name", required=True)

    manufacturer_id = fields.Many2one('mobile.phone.manufacturer', ondelete='cascade'
                                      , string="Manufacturer", index=True, required=True)
