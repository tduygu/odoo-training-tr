# -*- coding: utf-8 -*-
from odoo import http

# class Erpuygulamalar(http.Controller):
#     @http.route('/erpuygulamalar/erpuygulamalar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/erpuygulamalar/erpuygulamalar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('erpuygulamalar.listing', {
#             'root': '/erpuygulamalar/erpuygulamalar',
#             'objects': http.request.env['erpuygulamalar.erpuygulamalar'].search([]),
#         })

#     @http.route('/erpuygulamalar/erpuygulamalar/objects/<model("erpuygulamalar.erpuygulamalar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('erpuygulamalar.object', {
#             'object': obj
#         })