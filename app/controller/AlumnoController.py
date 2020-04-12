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

def crearAlumno(nombreAlumno,apellidoAlumno):
    res = {}
    objAlumno = Alumno(
        nombre= nombreAlumno,
        apellido_paterno = apellidoAlumno
    )
    Alumno().addOne(objAlumno)
    res['message'] = 'Se registro correctamente el alumno de id ' + str(objAlumno.id_alumno)
    return res

def obtenerAlumno(idAlumno):
    res = {}

    objAlumno = Alumno().getOne(idAlumno) # metodo devuelve un alumno

    if objAlumno != None:
        res['alumno'] = objAlumno.toJson()
    else:
        res['alumno'] = None 
    
    return res
