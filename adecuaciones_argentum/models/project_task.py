# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details

from odoo import api, models, fields


class Task(models.Model):
    _inherit = 'project.task'

    invoice_id = fields.Many2one('account.move', string='Factura', help='Factura asociada a la Tarea/Hito')
    parent_partner_id = fields.Many2one('res.partner', compute="_compute_parent_partner_id")
    
    @api.onchange('partner_id')
    def _compute_parent_partner_id(self):
        for record in self:    
            try:
                if record.partner_id.company_type == 'company':
                    self.parent_partner_id = self.partner_id
                else:
                    self.parent_partner_id = self.partner_id.parent_id if self.partner_id.parent_id else self.partner_id
            except:
                pass

    @api.onchange('date_deadline')
    def _update_invoice_date(self):
        for record in self:
            if record.date_deadline:
                record.invoice_id.write({'invoice_date': record.date_deadline})