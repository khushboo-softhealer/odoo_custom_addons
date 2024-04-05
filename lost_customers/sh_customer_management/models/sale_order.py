# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime

from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'


class ResCompany(models.Model):
    _inherit = 'res.company'

    
    lost_customer = fields.Boolean(
        string='Lost Customer',
        default=False
    )
    
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    
    lost_customer = fields.Boolean(
        string='Lost Customer',
        related='company_id.lost_customer',
        readonly=False
    )
    

