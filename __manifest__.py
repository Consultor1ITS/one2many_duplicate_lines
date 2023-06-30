{
    'name': 'One2Many Duplicate Lines',
    'author': 'Opsway',
    'version': '16.0.1.0',
    'website': 'https://www.opsway.com',
    'category': 'Extra Tools',
    'description': 'Module for duplicate lines in one2many fields',
    'summary': """
        This module adds a simple method for duplicating lines in one2many fields.
    """,
    'depends': ['web'],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend':[
            'one2many_duplicate_lines/static/src/**/*',
        ]
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
