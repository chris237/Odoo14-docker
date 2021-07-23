# -*- coding: utf-8 -*-
# Copyright 2021 Odoo Dev - Christian Ferdinand <fotie201@gmail.com>

{
    'name': "Send Email Quote without Price",
    'version': '0.1',
    'summary': """Send Quote without Price by Email""",
    'description': """This module allow send quote without price by mail""",
    'author': "Christian Ferdinand FOTIE",
    'company': "Christian Ferdinand FOTIE",
    'website': "",
    'category': 'Sale',
    'depends': ['base', 'sale', 'sale_management'],
    'data': [
        'views/send_quote.xml',
        'views/quote_mail_template.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
