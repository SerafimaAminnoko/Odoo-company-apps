# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
#             record.value2
#             float(record.value) / 100


class GlobalTasks(models.Model):
    _name = 'company_task_manager.global_tasks'
    _description = 'company_task_manager.global_tasks'

    name = fields.Char()
    description = fields.Text()
    data_add = fields.Datetime()
    data_closed = fields.Datetime()


class Employee(models.Model):
    _name = 'employees'
    _description = 'employees'

    name = fields.Char()
    data_add = fields.Datetime(default=fields.Datetime.now)


class Tasks(models.Model):
    _name = 'tasks'
    _description = 'tasks'

    title = fields.Char()
    description = fields.Text()
    time_create = fields.Datetime(default=fields.Datetime.now)
    employee_id = fields.Many2one("employees", string="Partner")
    status = fields.Selection(
        [('pending', 'Pending'), ('in process', 'In Process'),
         ('completed', 'Completed'), ('canceled', 'Canceled')]
    )
