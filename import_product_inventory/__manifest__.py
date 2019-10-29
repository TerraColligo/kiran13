{'name': 'Import product in Batch',
 'version': '13.1.28.10.2019',
 'summary': 'Mass import-export of products',
 'category': 'other',
 'depends': ['l10n_mx','l10n_mx_edi','sale_stock','purchase', 'point_of_sale'],
 'author': "Kiran Kantesariya",
 'license': 'OPL-1',
 'website': '',
 'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/cron.xml',
        'views/product_import_batch_view.xml',
        'views/product_cierries_import_batch_view.xml',
        'wizard/import_product_wizard_view.xml',
        'wizard/import_cierres_product_wizard_view.xml',
        'wizard/export_product_view.xml',
        ],
  "qweb": [
       "static/src/xml/base.xml",
        ],
 'installable': True,
 'application': True,
 }
