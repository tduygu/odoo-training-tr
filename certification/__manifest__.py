# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Certification",
    "summary": "Certification Management",
    'version': '12.0.1.0.0',
    "category": "Certification Management",
    "website": "https://github.com/tduygu",
    "author": "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    'application': False,
    'installable': True,
    'auto_install': False,
    "depends": [
        'base'
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/certification_view.xml',
        'views/standard_view.xml',
        'views/res_partner_view.xml'
    ],
    "demo":[
        'demo/certification_data.xml'
    ],
'development_status': 'Beta',
'maintainers': ['ceeficent']
}
