from odoo import fields, api, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    
    sh_count_report = fields.Integer(
        string='Count Report',
        default=0
    )
    
class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def _get_rendering_context(self, report, docids, data):

        print("\n\n",report,"\n",docids,"\n",data,"\n\n")
        res = super()._get_rendering_context(report, docids, data)
        
        print(res)
        
        sale_orders = self.env['sale.order'].search([('id','=',docids)])


        if report.report_name == "sale.report_saleorder_raw":
            for order in sale_orders:
                order.sh_count_report += 1
                
                msg = "Report printed by :- {user} \nTotal prints :- {count}".format(
                    user=self.env.user.name, 
                    count=order.sh_count_report
                )
                order.message_post(body=msg)
                print(msg)

        return res
