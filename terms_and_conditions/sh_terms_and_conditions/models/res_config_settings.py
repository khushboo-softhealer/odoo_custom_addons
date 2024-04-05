# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResCompany(models.Model):
    _inherit = 'res.company'

    is_terms = fields.Boolean(
        string='Terms And Conditions',
    )

    terms_and_conditions = fields.Html(
        string='Terms And Conditions',
    )
        
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
   
    is_terms = fields.Boolean(
        related='company_id.is_terms',
        readonly=False
    )
    
    terms_and_conditions = fields.Html(
        related='company_id.terms_and_conditions',
        readonly=False
    )
    
    @api.model
    def default_get(self, fields):
        res = super(ResConfigSettings, self).default_get(fields)
        
        res_company = self.env['res.company'].browse(res.get('company_id'))
        terms = res_company.terms_and_conditions
        
        if terms:
            sale_orders = self.env['sale.order'].search([])
            sale_orders.write(
                {
                    'note': terms
                }
            )
    
        return res
        
    
