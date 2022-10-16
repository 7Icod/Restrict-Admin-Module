# -*- coding: utf-8 -*-
{
    'name': "Restrict Admin",
    'summary': """
        This module will use to restrict admin from some devloper settings""",
    'description': """
        This module will use to restrict admin from some devloper settings
    """,
    'author': "Hamza - Holool AL-Ghad",
    'website': "http://www.holoolalghad.com",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        # 'views/users_restrict.xml',
        # 'static/src/developer_mode.xml',
        # 'static/src/base.xml'
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'sequence': '-201'
}
