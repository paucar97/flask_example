from app.models.Alumno import Alumno

def listarAlumnos():
    res = {}
    lst = []
    listaAlumnos = Alumno().getAll() # SELECT * FROM ALUMNOS

    for alumno in listaAlumnos:
        lst.append(alumno.toJson())

    res['lstAlumno'] = lst
    res['cantAlumno'] = len(lst)
    return res

"""
{
    lstAlumno:[

    ]

}
"""