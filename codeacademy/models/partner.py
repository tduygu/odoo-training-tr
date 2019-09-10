# -*- coding: utf-8 -*-

from odoo import api, models, modules, fields


class Partner(models.Model):
    _inherit = ['res.partner']
    _name = 'codeacademy.partner'
    _description = 'description'

    is_instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many('codeacademy.session', string="Attended Sessions", readonly=True)



