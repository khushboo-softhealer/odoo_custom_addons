# -*- coding: utf-8 -*-
# Softhealer Technologies.

{
    'name' : 'Report Count',
    'version' : '17.0.1.0.1',
    'summary': 'Module for Report Count',
    'sequence': 10,
    'description': "Report Count module.",
    'category': 'Extra tools',
    'depends': ['base_setup', 'web','sale', 'base'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/note_view.xml',
        'views/sale_order_qweb.xml',
        # 'views/res_partner_view.xml',
        'views/sale_order_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True
}
