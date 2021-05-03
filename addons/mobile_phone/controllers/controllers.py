# -*- coding: utf-8 -*-
# from odoo import http


# class MobilePhone(http.Controller):
#     @http.route('/mobile_phone/mobile_phone/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mobile_phone/mobile_phone/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mobile_phone.listing', {
#             'root': '/mobile_phone/mobile_phone',
#             'objects': http.request.env['mobile_phone.mobile_phone'].search([]),
#         })

#     @http.route('/mobile_phone/mobile_phone/objects/<model("mobile_phone.mobile_phone"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mobile_phone.object', {
#             'object': obj
#         })
