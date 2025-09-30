from odoo import models, fields

class Enrollment(models.Model):
    _name = 'school.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    enroll_date = fields.Date(default=fields.Date.today)
