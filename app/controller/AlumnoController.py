from app.models.Alumno import Alumno
from app.dto.ListaAlumnoDTO import ListaAlumnoDTO
from app.data_access.alumno_acceso_datos import AlumnoAccesoDatos


def listarAlumnos():
    res = {}
    lst = []
    alumnosDA = AlumnoAccesoDatos()
    listaAlumnos = alumnosDA.listar_todos_alumnos() # SELECT * FROM ALUMNOS
    # Supongo que aqui iria la logica de negocios no?
    """for alumno in listaAlumnos:
        lst.append(alumno.toJson())

    res['lstAlumno'] = lst
    res['cantAlumno'] = len(lst)
    return res"""
    return ListaAlumnoDTO(listaAlumnos, len(listaAlumnos))

"""
{
    lstAlumno:[

    ]

}
"""