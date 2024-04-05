# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import timedelta, datetime


class LostCustomerWizard(models.TransientModel):
    _name = 'lost.customer.wizard'
    _description = _('LostCustomerWizard')

    name = fields.Char(_('Name'))
    
    res_partner_ids = fields.Many2many(
        string='Lost Customers',
        comodel_name='res.partner',
        readonly=True
    )
    
    fetch_lost_customer_ids = fields.One2many(
        'fetch.lost.customer',
        'lost_customer_wizard_id',
        string='Lost Customer'
    )

    
    @api.model
    def default_get(self, fields):
        res = super(LostCustomerWizard, self).default_get(fields)
    
        all_customers = self.env['res.partner'].search([])
        total_orders = self.env['sale.order'].search(
            [
                '&',
                ('date_order', '>=', (datetime.now() - timedelta(days=6))),
                ('state', '=', 'sale')
            ]
        )

        lost_customers = all_customers - total_orders.partner_id
        
        print('\n\n',(datetime.now() - timedelta(days=6)), '\n\n', total_orders, '\n\n', all_customers, '\n\n', lost_customers)
        
        res['res_partner_ids'] = [(6, 0, lost_customers.ids)]
        
        for customer in lost_customers:
            customer_information = self.env['fetch.lost.customer']

        
        # for customer in lost_customers:
        #     alert = self.env['fetch.lost.customer'].create(
        #         {
        #             'customer_id': customer.id,
        #             'order_date': customer.date_order,
        #         }
        #     )

        #     alert_assign += alert



        return res
        
    

    def add(self):
        pass
