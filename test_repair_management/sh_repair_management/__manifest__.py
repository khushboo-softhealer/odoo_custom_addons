# -*- coding: utf-8 -*-
# Softhealer Technologies.

{
    'name' : 'Repair Management System',
    'version' : '17.0.1.0.1',
    'summary': 'Module for Repair management',
    'sequence': 1,
    'description': "Repair Management module.",
    'category': 'Extra tools',
    'depends': ['base_setup', 'web', 'base', 'product', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',

        # 'report/ir_actions_report_templates.xml',
        # 'report/ir_actions_report.xml',

        # 'wizard/student_get_complaint_view.xml',
        # 'wizard/student_fire_note_view.xml',
        # 'wizard/set_default_partner_view.xml',
        # 'wizard/alert_view.xml',

        'views/repair_request_view.xml',
        'views/repair_request_line_view.xml',
        # 'views/faculty_view.xml',
        # 'views/student_age_category_view.xml',
        # 'views/student_fees_view.xml',
        # 'views/school_view.xml',
        # 'views/result_view.xml',
        # 'views/course_view.xml',
        # 'views/contact_inherit_view.xml',
        # 'views/student_fire_reason_view.xml',
        # 'views/student_complaint_view.xml',
        'views/repair_menu_view.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True
}
