# -*- coding: utf-8 -*-
{
    'name': "Amount To Text",

    'summary': """
        Transforme le montant en lettres sur les factures""",

    'description': """
        Ajoute un champs transformant le montant total d'une factures, en lettres et ajoute l'affichage sur les impressions de factures
    """,

    'author': "Nacim Aboura",
    'website': "http://www.igpro-online.net",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_voucher'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'reports.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
