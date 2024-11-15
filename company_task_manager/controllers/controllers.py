# -*- coding: utf-8 -*-
# from odoo import http


# class CompanyTaskManager(http.Controller):
#     @http.route('/company_task_manager/company_task_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_task_manager/company_task_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_task_manager.listing', {
#             'root': '/company_task_manager/company_task_manager',
#             'objects': http.request.env['company_task_manager.company_task_manager'].search([]),
#         })

#     @http.route('/company_task_manager/company_task_manager/objects/<model("company_task_manager.company_task_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_task_manager.object', {
#             'object': obj
#         })

