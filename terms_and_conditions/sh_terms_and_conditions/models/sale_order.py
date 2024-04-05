# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def default_get(self, fields):
        res = super(SaleOrder, self).default_get(fields)
        
        # company = self.env['res.company'].browse(res.get('company_id'))

        terms_and_condition = self.env['res.config.settings'].search(
            domain = [
                ('is_terms', '=', True)
            ],
            order= 'id desc',
            limit=1,
        )
        res['note'] = terms_and_condition.terms_and_conditions
        
        return res
    

    
    
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, values):
        """
            Create a new record for a model StockPicking
            @param values: provides a data for new record
    
            @return: returns a id of new record
        """

        result = super(StockPicking, self).create(values)

        sale_order = self.env['sale.order'].search([('name', '=', result.origin)])

        result.note = sale_order.note

        return result
    