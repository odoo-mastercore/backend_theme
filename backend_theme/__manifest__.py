# -*- coding: utf-8 -*-
# Copyright 2020-2021 MASTERCORE
# Special Thanks to Mario Gielissen Openwork Material Backend Theme V14
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Simplified emulated EE Backend Theme",
    "summary": "Simplified emulated EE Backend Theme",
    "version": "14.0.1.0",
    "category": "Theme/Backend",
    "website": "https://www.openworx.nl",
	"description": """
		Simplified emulated EE Backend Theme for Odoo 14.0 CE
        Special Thanks to Mario Gielissen Openwork Material Backend Theme V14
    """,
	"author": "Openworx, MASTERCORE SAS || SINAPSYS GLOBAL SA",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'web_responsive',

    ],
    "data": [
        'views/assets.xml',
		'views/res_company_view.xml',
		'views/users.xml',
        	'views/sidebar.xml',
    ],
}

