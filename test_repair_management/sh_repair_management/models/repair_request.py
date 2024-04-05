from odoo import _, api, fields, models


class RepairRequest(models.Model):
    _name = 'sh.request.repair'
    _description = 'Repair Request Details'

    
    name = fields.Char(
        string='Request ID',
        required=True
    )
    

    customer_id = fields.Many2one(
        string='Customer',
        comodel_name='res.partner',
        required=True,
        
        domain=[('customer_rank','>',0)]
        
    )
    
    request_date = fields.Datetime(
        string='Request Date',
        default=fields.Datetime.now,
    )

    responsible_user_id = fields.Many2one(
        string='Responsible User',
        comodel_name='res.users',
        readonly=True,
        default=lambda self: self.env.user
        
    )
    
    state = fields.Selection(
        string='Status',
        selection=[
            ('draft', 'Draft'),
            ('sent', 'Confirm'),
            ('sale', 'Order Created')
        ],
        default='draft'
    )

    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True, index=True,
        default=lambda self: self.env.company)
    
    request_line_ids = fields.One2many('sh.repair.request.line', 'repair_id', string='Request Line')

    def action_confirm(self):

        if self.state == 'sent':
            self.state = 'draft'

        elif self.state != 'sent':
            self.state = 'sent'

    def action_create_order(self):
        if self.state == 'sent':
            self.state = 'sale'

            sale_order = self.env['sale.order'].create(
                {
                    'name':self.name,
                    'company_id': self.company_id.id,
                    'partner_id': self.customer_id.id,
                    'date_order': self.request_date,
                    'partner_invoice_id': self.customer_id.address_get(['invoice'])['invoice'] if self.customer_id else False,
                    'partner_shipping_id': self.customer_id.address_get(['delivery'])['delivery'] if self.customer_id else False,
                    'user_id': self.responsible_user_id.id,
                }
            )

            sale_order_line = self.env['sale.order.line']
            request_lines = self.env['sh.repair.request.line'].browse(self.request_line_ids.ids)
            print(request_lines)
            for line in request_lines:
                sale_order_line += self.env['sale.order.line'].create(
                    {
                        'order_id': sale_order.id,
                        'name': line.name,
                        'product_uom_qty': line.quantity,
                        'price_unit': line.repair_charge,
                        'customer_lead':False,
                        'product_id': line.product_id.id,
                    }
                )

