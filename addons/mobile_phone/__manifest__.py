# -*- coding: utf-8 -*-
{
    'name': "mobile_phone",

    'summary': "System for selling mobile phones",

    'description': """
        Module adds new fields to the product form (Manufacturer and Model) and allows 
        to quickly create products using wizard  
    """,

    'author': "Morozov Yuri",
    'website': "https://github.com/yurimorozov/odoo-test-task",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/mobile_wizard_view.xml',
        'views/mobile_phone.xml',
        'views/product_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
