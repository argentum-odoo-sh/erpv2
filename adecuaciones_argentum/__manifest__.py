{
    "name": "Adecuaciones Argentum",
    "summary": """
        Adecuaciones para Argentum""",
    "author": "ARGENTUM Inc S.R.L.",
    "category": "Base",
    "version": "15",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale_management", "sale_crm", "account", "account_accountant"],
    # always loaded
    "data": [
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
    ],
    
}
