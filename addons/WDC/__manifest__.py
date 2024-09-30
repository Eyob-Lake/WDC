{
    "name": "Wudasie Diagnostic Center",
    "version": "0.0.1",
    "author": "Fetun Technology Solution",
    "license": "LGPL-3",
    "category": "Healthcare",
    "summary": "Module for managing patient records and diagnostics.",
    "description": """
        This module provides functionality for managing patient records,
        including personal information, visit history, and prescriptions.
    """,
    "depends": [
        "base",
        "contacts","mail",
    ],
    "images": [
        "static/description/wdc_logo.png",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/patient_views.xml",
        "views/menu.xml",
        # "static/src/css/custom_style.css",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "website": "https://wudassie.net"
}
