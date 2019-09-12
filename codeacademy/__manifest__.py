# -*- coding: utf-8 -*-
{
    'name': "Code Academy",

    'summary': """Manage Trainings""",

    'description': """
        Code Academy Courses for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Duygu",
    'website': "http://www.codeacademy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/codeacademy.xml',
        'views/partner.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}