# Odoo
El proyecto gestiona una lista de alumnos, programas e inscripciones, las cuales están relacionadas entre sí.  
Las mismas pueden verse, filtrarse y crearse a traves de una vista del tipo lista, formulario y de búsqueda.  
Contiene un controlador en la ruta:  
{PATH_SERVER}/inscripcion?programa_id={id_del_programa}  
la cual al recibir un get, devuelve un JSON con información de los alumnos inscriptos en un programa determinado.
