# -*- coding: utf-8 -*-

from odoo import models, fields, api


class School(models.Model):
    _name = 'wb.school'
    _description = 'This is a school profile'

    invoice_id = fields.Many2one("account.move")
    invoice_user_id = fields.Many2one("res.users")
    invoice_date = fields.Date(related="invoice_id.invoice_date", store=True)
    name = fields.Char("Name")
    school_list = fields.One2many('wb.student', 'school_id')
    ref_field_id = fields.Reference([
        ("wb.school", 'School'),
        ("wb.student", 'Student'),
        ("wb.hobby", 'Hobby'),
    ])

    binary_field = fields.Binary("Binary Field")
    binary_file_name = fields.Char("Binary File Name")
    binary_fields = fields.Many2many("ir.attachment")
    currency = fields.Many2one("res.currency", by_default=1)
    amount = fields.Monetary("Amount", currency_field="currency")
    school_image = fields.Image("School Image", max_width=128, max_length=128)

    def unlink(self):
        rtn = super(School, self).unlink()
        print(rtn)
        return rtn

   # @api.model
    @api.model_create_multi
    def create(self, vals):
        print(self)
        print(vals)
   #     rtn = super(School, self).create(vals)
        rtn = super().create(vals)
        print(rtn)
        return rtn

    def custom_method(self):
#        print("Custom method clicked!")
#        print(self)
#        self.name = "Single Update"
#        self.amount = 50
#        self.write({"name": "Write", "amount": 40})

        records = self.search([("amount", "=", 40)])
        print(records)
#        print(records)

#        records.write({"name": "mass editing name", "amount": 1000})

#        for rec in records:
#            rec.write({"name": f"{rec.id}", "amount": 40})

        # select * from school where amount = 100;
#        records = self.search([("amount", "=", 40)])
    #    self.print_table(records)


    def write(self, vals):
        print("Write method called!")
        print(self)
        rtn = super(School, self).write(vals)
        print(vals)
        print(rtn)


class Student(models.Model):
    _name = 'wb.student'
    _description = 'This is a student profile'

    def delete_records(self):
        print(self)
        school_id = self.env["wb.school"].browse(23)
        print(school_id)
        print(school_id.unlink())


    def duplicate_records(self):
        print(self)
        duplicate_record = self.copy({"joining_date": fields.Datetime.now()})
        print(duplicate_record)

    def copy(self, default=None):
        print(self)
        print(default)
        return super(Student, self).copy(default=default)


    hobby_list = fields.Many2many("wb.hobby", "student_hobby_list_relation", "student_id", "hobby_id")
    school_id = fields.Many2one(comodel_name="wb.school", help='Please choose your school')
    joining_date = fields.Datetime(default=fields.Datetime.now)
    school_data = fields.Json()
    student_fees = fields.Float(digits=(4, 2), default=6.9, required=True)
    discount_fees = fields.Float(digits=(4, 2), default=3.2, required=True)
    roll_number = fields.Integer('Integer')
    gender = fields.Selection(
        [('female', 'Female'), ('male', 'Male')]
    )
    advance_gender = fields.Selection("_get_advance_gender_list")
    name = fields.Char('Name')
    is_paid = fields.Boolean('-> Paid?')
    name1 = fields.Char('Name1')
    name2 = fields.Char('Name2', copy=True)
    name3 = fields.Char('Name3', default='Dadu')
    name4 = fields.Char('Name4', readonly=True)
    student_name = fields.Char(index=True, size=5)
    address = fields.Text('Address', help='Enter here student address')
    address_html = fields.Html("Address Html")
    image = fields.Image(string='Image')

    final_fees = fields.Float("Final Fees", compute="_compute_final_fees_call", store=True)


    def send_email_template(self):
        self.env.ref("Wcustom_email_template.Wstudent_email_template").send_mail(self.id, force_send=True)



    def return_string_from_backend_to_emailtemplate(self):
        return "Weblearns"

    def _compute_final_fees_call(self):
        for record in self:
            record.final_fees = record.student_fees - record.discount_fees

    def json_data_store(self):
        self.school_data = {"name": self.name,
                            "id": self.roll_number,
                            "fees": self.student_fees}

    def _get_advance_gender_list(self):
        return [('female', 'Female'), ('male', 'Male')]

    def custom_method(self):
        data = {"name": "Weblearns"}

        self.env["wb.school"].create(data)


class Hobby(models.Model):
    _name = 'wb.hobby'
    _description = 'This is a hobby profile'

    name = fields.Char("Name")

