# -*- coding: utf-8 -*-
# Copyright 2020 MASTERCORE
# Thanks Openwork Material Backend Theme V13
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "MASTERCORE Simplified Material Backend Theme",
    "summary": "MASTERCORE Simplified Material Backend Theme",
    "version": "13.0.0.1",
    "category": "Theme/Backend",
    "website": "https://mastercore.net",
	"description": """
		MASTERCORE Simplified Material Backend theme for Odoo 13.0 CE
        Thanks to Openwork Material Backend Theme V13
    """,
	'images':[
        'images/screen.png'
	],
    "author": "MASTERCORE SAS || SINAPSYS GLOBAL SA",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'web_responsive',

    ],
    "data": [
        'views/assets.xml',
		# 'views/res_company_view.xml',
    ],
}

