# -*- coding: utf-8 -*-
{
    'name': 'Customer Management',
    'version': '17.0.1.0',
    'description': """ Customer Description """,
    'summary': """ Customer Summary """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web', 'sale'],
    "data": [
        "security/access_groups.xml",
        "security/ir.model.access.csv",
        
        "wizards/lost_customer_wizard.xml",
        "wizards/fetch_lost_customer.xml",
        "views/res_config_settings_views.xml",
        "views/customer_menu.xml",
    ],
    'assets': {},
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
