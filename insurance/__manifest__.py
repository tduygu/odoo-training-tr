# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Insurance MAnagement System",
    "summary": "Insurance management issues are being handled.",
    'version': '12.0.1.0.0',
    "category": "Insurance Management",
    "website": "https://github.com/tduygu",
    "author": "Eren, Duygu, Özgür - ÖDE",
    "license": "AGPL-3",
    'application': True,
    'installable': True,
    'auto_install': False,
    "depends": [
        'base'
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/Insurance_view.xml',
    ],
}
