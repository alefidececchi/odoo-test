{
    'name': "Aden",
    'version': '1.0',
    'depends': ['base'],
    'author': "Alejandro Fidececchi",
    'category': 'Education',
    'description': "Aplicación que gestiona alumnos, programas e inscripciones de la institución.",
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/menu_aden.xml',
        'views/alumno_view.xml',
        'views/programa_view.xml',
        'views/inscripcion_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}

