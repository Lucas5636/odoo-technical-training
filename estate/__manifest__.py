{
    "name": "Estate",  # The name that will appear in the App list
    "version": "16.0.0",  # Version
    "author": "Langue Lucas",
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
	"views/estate_menus.xml",
    ],
    'demo':[

    ],
    "installable": True,
    'license': 'LGPL-3',
}
