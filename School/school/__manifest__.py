{
    'name': "Daffodil School",
    'author': "Imran",
    'website': "https://www.dis.edu.bd/",

    'category': 'erp',
    'version': '1.0',

    # always loaded
    'data': [

        # Views
        'views/student.xml',
        'views/teacher.xml',
        'views/section.xml',
        'views/registration.xml',
        'views/course.xml',

        # Security
        'security/ir.model.access.csv',

        # Menu
        'views/menu.xml',

    ],

}
