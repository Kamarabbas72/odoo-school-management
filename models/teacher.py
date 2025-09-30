from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(required=True)
    subject = fields.Char()
    hire_date = fields.Date(default=fields.Date.today)
