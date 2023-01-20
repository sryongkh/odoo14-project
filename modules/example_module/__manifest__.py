# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'SFs Stock',
    'version' : '1.0',
    'depends' : ["base", "stock","sale_stock","purchase_stock"],
    'category': 'SFS',
    "summary" : "Edit create products   ",
    'author': 'Simply & Fine Solutions',
    'website': 'http://www.sfsolutions.co.th/',
    'description': """
    """,
    'data': [
        'data/ir_scheduler_data.xml',
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/stock_picking_api_log_view.xml',
        'views/stock_picking.xml',
        'views/stock_location_view.xml',
        'views/stock_warehouse_view.xml',
        'views/uom_uom_view.xml',
        'views/purchase_order_views.xml',
        'views/stock_inventory_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': [],
}

