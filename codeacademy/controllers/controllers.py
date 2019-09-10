# -*- coding: utf-8 -*-
from odoo import http

# class Codeacademy(http.Controller):
#     @http.route('/codeacademy/codeacademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/codeacademy/codeacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('codeacademy.listing', {
#             'root': '/codeacademy/codeacademy',
#             'objects': http.request.env['codeacademy.codeacademy'].search([]),
#         })

#     @http.route('/codeacademy/codeacademy/objects/<model("codeacademy.codeacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('codeacademy.object', {
#             'object': obj
#         })