{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage Students in Odoo',
    'author': 'Kamarabbas Bukhari',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'views/student_views.xml',
        'security/ir.model.access.csv',
            
    
    ],
    'installable': True,
    'application': True,
}
