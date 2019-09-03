# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests import api

from odoo import fields, models





class ResPartner(models.Model):
    _inherit = 'res.partner'

    # _name = 'res.deneme'

    is_certification_body = fields.Boolean(string = "Is certification body?", help = "indicates if the contact has a certification body", default=True)
    certification_ids = fields.One2many(comodel_name='certification', inverse_name='owner_id')




    # is_test = fields.Boolean(string = "Test field", help = "test abc test")
