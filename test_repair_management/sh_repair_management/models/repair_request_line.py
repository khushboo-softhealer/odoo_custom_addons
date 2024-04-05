from odoo import api, fields, models


class RepairRequestLine(models.Model):
    _name = 'sh.repair.request.line'
    _description = 'Repair Request Line Detail'

    
    name = fields.Text(
        string='Description',
        compute="_compute_name"
    )
    
    product_id = fields.Many2one(
        string='Parts',
        comodel_name='product.product',
        default=False,
        domain=[('detailed_type','=','service')]
    )

    
    quantity = fields.Integer(
        string='Quantity',
        default=1
    )
    
    
    repair_charge = fields.Float(
        string='Repair Charge',
        related='product_id.lst_price'
    )
    
    
    repair_id = fields.Many2one(
        string='Repair',
        comodel_name='sh.request.repair',
    )
    
    tax_ids = fields.Many2many(
        string='Tax',
        comodel_name='account.tax',
        related='product_id.taxes_id'
    )

    
    sub_total = fields.Float(
        string='Sub Total',
        compute="_compute_subtotal"
    )
    
    
    @api.depends('product_id')
    def _compute_name(self):
        for record in self:
            record.name=False
            name = ""
            if record.product_id:
                if record.product_id.description_sale:
                   name = record.product_id.name + '\n' + record.product_id.description_sale
                else:
                    name = record.product_id.name
            record.name = name

    @api.depends('quantity','product_id')
    def _compute_subtotal(self):
        for record in self:
            sub_total = 0
            if record.quantity:
                sub_total = record.quantity * record.repair_charge
            record.sub_total = sub_total

   
