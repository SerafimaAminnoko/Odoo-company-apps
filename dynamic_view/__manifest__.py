{
    'name': 'Dynamic View',

    'author': 'Weblearns Channel',
    'summary': 'Custom First Dynamic View',
    'sequence': 1,
    'website': "https://www.yourcompany.com",

    'category': 'Company',
    'version': '1.1',
    'depends': ['base', 'student'],

    'data': [
        'security/ir.model.access.csv',
        'views/dynamic_view.xml',
    ]
}