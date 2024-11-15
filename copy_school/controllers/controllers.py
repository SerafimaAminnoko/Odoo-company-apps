# -*- coding: utf-8 -*-
# from odoo import http


# class CopySchool(http.Controller):
#     @http.route('/copy_school/copy_school', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/copy_school/copy_school/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('copy_school.listing', {
#             'root': '/copy_school/copy_school',
#             'objects': http.request.env['copy_school.copy_school'].search([]),
#         })

#     @http.route('/copy_school/copy_school/objects/<model("copy_school.copy_school"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('copy_school.object', {
#             'object': obj
#         })

