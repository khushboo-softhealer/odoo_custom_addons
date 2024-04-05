# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class FetchLostCustomer(models.TransientModel):
    _name = 'fetch.lost.customer'
    _description = _('FetchLostCustomer')

    name = fields.Char(_('Name'))
    
    customer_id = fields.Many2one(
        string='Customer',
        comodel_name='res.partner',
    )
    
    order_date = fields.Datetime(
        string='Order Date',
    )
    
    lost_customer_wizard_id = fields.Many2one(
        string='Lost Customer Wizard',
        comodel_name='lost.customer.wizard',
    )
    
    def add(self):
        pass
