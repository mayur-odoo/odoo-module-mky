# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'school Management',
    'version': '1',
    'category': 'school',
    'summary': 'Scool informtion',
    'description': """
This module contains all the informtion of the school.
    """,
    'depends': ['sale_management', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/student_detail_views.xml',
        'views/sale_order_view.xml',
        'views/school_view.xml',
        'views/femel_studnet.xml',
    ],
    'installable': True,
    'auto_install': False,
}