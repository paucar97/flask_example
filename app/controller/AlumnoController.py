from app.models.Alumno import Alumno
from app.dto.AlumnoDTO import AlumnoDTO
from app.dto.ListaAlumnoDTO import ListaAlumnoDTO
from app.data_access.alumno_acceso_datos import AlumnoAccesoDatos
from flask import abort, jsonify

def listarAlumnos():
    res = {}
    lst = []
    alumnosDA = AlumnoAccesoDatos()
    listaAlumnos = alumnosDA.listar_todos_alumnos() # SELECT * FROM ALUMNOS
    return jsonify(code=200, data=ListaAlumnoDTO(listaAlumnos, len(listaAlumnos)).toJson(), message='Alumnos obtenidos con exito')
    

def crearAlumno(alumnoDTO):
    res = {}
    obj_alumno = Alumno(
        nombre= alumnoDTO.nombre,
        apellido_paterno = alumnoDTO.apellido
    )
    alumnosDA = AlumnoAccesoDatos()
    alumnosDA.agregar_un_alumno(obj_alumno)
    rptaDTO = AlumnoDTO(obj_alumno.id_alumno, obj_alumno.nombre, obj_alumno.apellido_paterno)
    return jsonify(code=200, data=rptaDTO.toJson(), message=f'Se registro correctamente el alumno de id {obj_alumno.id_alumno}')


def obtenerAlumno(idAlumno):
    res = {}
    alumnosDA = AlumnoAccesoDatos()
    obj_alumno = alumnosDA.obtener_alumno_por_id(idAlumno) # metodo devuelve un alumno
    if obj_alumno != None:
        rptaDTO = AlumnoDTO(obj_alumno.id_alumno, obj_alumno.nombre, obj_alumno.apellido_paterno)
        return jsonify(code=200, data=rptaDTO.toJson(), message='Alumno encontrado con exito')
    else:
        abort(404, 'Error: Alumno no encontrado')
