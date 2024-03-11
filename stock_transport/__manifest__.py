{
    "name": "Stock Transport",
    "depends": [
        "fleet",
        "stock_picking_batch",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/fleet_views.xml",
        "views/stock_views.xml",
    ],
    "auto_install": True,
}