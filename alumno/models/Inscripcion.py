from odoo import fields,models


class Inscripcion(models.Model):

    _name = 'inscripcion'
    _description = 'Inscripción'
    _register = True

    alumno_id = fields.Many2one(
        'alumno',
        String="Alumno",
        required=True
    )
    programa_id = fields.Many2one(
        'programa',
        string="Programa",
        required=True
    )
