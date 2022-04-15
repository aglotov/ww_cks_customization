# -*- coding: utf-8 -*-
#################################################################################
# Author      : White Wind Ltd. (<https://wwind.ua/>)
# Copyright(c): 2022-White Wind Ltd.
# All Rights Reserved.
#################################################################################
{
    'name': "CKS Customization",

    'summary': """Customization exclusively for the needs of CKS company""",

    'description': """
        Changed partners form.
        Changed crm.lead form.
    """,

    'author': "White Wind LLC",
    'website': "https://wwind.ua",

    'category': 'Uncategorized',
    'version': '14.0.1.0.0',
    'depends': ['base', 'crm', ],
    'data': [
        'views/res_partner_views.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
}
