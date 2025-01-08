# -*- coding: utf-8 -*-

from odoo import models, fields



class Employee(models.Model):
    _name = 'employee'
    _description = 'employee'

    name = fields.Char('Name', required=True)
    email = fields.Char('Email', required=True)
    status = fields.Selection(
                              [('active', 'Active'),
                               ('inactive', 'Inactive')],
                              required=True)

    def send_mail(self):
        template = self.env.ref('compliment.template')
        template.send_mail(self.id, force_send=True)
