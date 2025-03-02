# -*- coding: utf-8 -*-
{
    'name': 'ERP Uygulamalar',
    'version': '1.0',
    'summary': """ERP Uygulamalar'a ait linkleri içerir.""",
    'sequence': 15,
    'author': "Duygu Tuncay Sanal",

    'description': """
        Long description of module's purpose
    """,
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/erpuygulamalar.xml',
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