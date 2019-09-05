from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Insurance(models.Model):
    _name = 'insurance.paymentplan'
    _description = 'Insurance Payment Plan'

    name = fields.Char()
    amount = fields.Float(digits=(6, 2), help="Amount to be paid", string="Installment")
    policy_id = fields.Many2one("insurance.policy",string="Policy")
    period = fields.Selection(
        [('january', "January"),
         ('february', "February"),
         ('march', "March"),
         ('april', "April"),
         ('may', "May"),
         ], 'Period',
        required=True)
    paid = fields.Boolean('Paid?', default=False)