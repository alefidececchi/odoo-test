from odoo import fields, models



class Programa(models.Model):


    _name = 'programa'
    _register = True
    _description = 'Programa'
    _order = 'id'

    nombre = fields.Char(
        "Nombre",
        size=45,
        required=True,
    )
    descripcion = fields.Text(
        "Descripción",
        required=True
    )


