from odoo import api, fields, models


class Alumno(models.Model):

    _name = 'alumno'
    # _log_access
    _register = True
    _description = 'Alumnos'
    _order = 'legajo'

    nombre = fields.Char(
        string="Nombre",
        required=True,
        default=None,
        # groups = [xml ids]
        store=True
    )
    apellido = fields.Char(
        string="Apellido",
        required=True,
        default=None,
        store=True
    )
    fecha_nacim = fields.Date(
        string="Fecha de nacimiento",
        required=True,
        default=None,
        store=True
    )
    legajo = fields.Integer(
        'Legajo',
        required=True,
        default=None,
        store=True
    )
    email = fields.Char(
        string="Email",
        required=True,
        default=None,
        store=True
    )
    telefono = fields.Char(
        string="Telefono",
        required=True,
        default=None,
        store=True
    )
    direccion = fields.Char(
        string="Dirección",
        required=False,
        default=None,
        store=True
    )
    pais_id = fields.Many2one(
        'res.country',
        string="ID pais",
        required=True,
        default=None,
        store=True
    )