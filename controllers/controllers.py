# -*- coding: utf-8 -*-
# from odoo import http


# class Reciclaje(http.Controller):
#     @http.route('/reciclaje/reciclaje', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reciclaje/reciclaje/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reciclaje.listing', {
#             'root': '/reciclaje/reciclaje',
#             'objects': http.request.env['reciclaje.reciclaje'].search([]),
#         })

#     @http.route('/reciclaje/reciclaje/objects/<model("reciclaje.reciclaje"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reciclaje.object', {
#             'object': obj
#         })
