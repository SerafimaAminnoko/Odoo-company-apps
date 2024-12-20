from odoo import fields, models, api, _, tools


class StudentDynamicView(models.Model):
    _name = 'dynamic'
    _description = 'This is the model for dynamic view'
    _auto = False

    school_name = fields.Char('School Name')
    school_email = fields.Char('School Email')
    school_phone = fields.Char('School Phone')
    school_type = fields.Selection([
        ('public', 'Public School'),
        ('private', 'Private School')],
        string='Type of School')
    student_name = fields.Char('Student Name')
    student_rno = fields.Char('Student Name')
    student_fees = fields.Float(string="Student Fees",
                                   index=True)


    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
        create or replace view {} as (
          select 
            std.id as id,
            std.roll_number as student_rno,
            std.name as student_name,
            std.student_fees as student_fees,
             sp.name as school_name,
             sp.email as school_email,
             sp.phone as school_phone,
             sp.school_type
             from wb_student as std join wb_school as sp on std.school_id=sp.id)
        """.format(self._table))
