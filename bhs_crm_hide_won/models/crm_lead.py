# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class Lead(models.Model):
    _inherit = 'crm.lead'

    hide = fields.Boolean(string='Hide this Opportunity')

    def action_hide(self):
        for rec in self:
            rec.hide = True

    def action_unhide(self):
        for rec in self:
            rec.hide = False
