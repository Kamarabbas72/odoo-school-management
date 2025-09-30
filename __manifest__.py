{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage Students in Odoo',
    'author': 'Kamarabbas Bukhari',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/course_views.xml',
        'views/enrollment_views.xml',
            
    
    ],
    'installable': True,
    'application': True,
}
