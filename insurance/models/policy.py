from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Insurance(models.Model):
    _name = 'insurance.policy'
    _description = 'Insurance Policy'

    name = fields.Char(string='Policy No', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    description = fields.Text(string='Policy Details')
    date_of_issue = fields.Date(string='Date of issue')
    vendor_id = fields.Many2one("res.partner", domain=[('is_company','=','True')], required=True)
    type = fields.Selection([('health', "Health"),('transport', "Transport"),('life','Life'),('na', "Not Applicable")],'Policy Type')
    paymentplan_ids = fields.One2many(comodel_name = 'insurance.paymentplan', inverse_name = 'policy_id')

    total_amount = fields.Float(string="Total Amount", required=True)
    total_payment = fields.Float(string="Total Payment", compute='_get_paid_value', store = True)


    @api.depends('total_amount', 'paymentplan_ids')
    def _get_paid_value(self):
         if(len(self.paymentplan_ids) == 0):
             self.total_payment = 0.0
         else:
             tpay = 0.0
             for pid in self.paymentplan_ids:
                tpay += pid.amount
             self.total_payment = tpay

    @api.constrains('total_payment', 'total_amount')
    def _check_total_amount(self):
        if self.total_payment > self.total_amount:
            raise ValidationError("Sum of payment plan amounts can't exceed total amount.")

    # @api.multi
    # def action_approve(self):
    #     current_employee = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
    #     for i in self:
    #         i.write({'state': 'validate', 'second_approver_id': current_employee.id})
    #     #	Eğer şu anki state validate1 ise state'i refuse olarak değiştirilir.
    #     return True

    # @api.depends('seats', 'attendee_ids')
    # def _taken_seats(self):
    #     for r in self:
    #         if not r.seats:
    #             r.taken_seats = 0.0
    #         else:
    #             r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats