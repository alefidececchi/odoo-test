from odoo import http
from odoo.http import Controller, request, route


class InscripcionController(Controller):
    @route('/inscripcion', type='http', auth='public', methods=['GET'])
    def get_inscripciones(self):
        programa_id = request.params.get('programa_id')
        alumnos = []

        if programa_id:
            try:
                inscripciones = request.env['inscripcion'].search([('programa_id', '=', int(programa_id))])
                for inscripcion in inscripciones:
                    alumno = inscripcion.alumno_id
                    alumnos.append({
                        'nombre': alumno.nombre,
                        'apellido': alumno.apellido,
                        'legajo': alumno.legajo,
                        'fecha_nacimiento': alumno.fecha_nacim,
                        'email': alumno.email,
                        'telefono': alumno.telefono,
                        'direccion': alumno.direccion,
                        'pais': {
                            'id': alumno.pais_id.id,
                            'nombre': alumno.pais_id.name
                        }
                    })
                return request.make_json_response(alumnos)
            except Exception as e:
                return request.make_json_response({'error': e.args, 'status': 500})
