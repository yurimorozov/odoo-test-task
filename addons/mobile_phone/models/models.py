# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mobile_phone(models.Model):
#     _name = 'mob ile_phone.mobile_phone'
#     _description = 'mobile_phone.mobile_phone'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
