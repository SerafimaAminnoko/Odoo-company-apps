# -*- coding: utf-8 -*-

# from odoo import models, fields, api


#class company_task_manager(models.Model):
#     _name = 'company_task_manager.company_task_manager'
#     _description = 'company_task_manager.company_task_manager'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

