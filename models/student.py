from odoo import models, fields

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student Record'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    grade = fields.Selection(
        [('a', 'Grade A'), ('b', 'Grade B'), ('c', 'Grade C')],
        string="Grade"
    )
    enrolled_date = fields.Date(string="Enrolled Date", default=fields.Date.today)
    active = fields.Boolean(string="Active", default=True)
