from app.models.Alumno import Alumno
from typing import List


class AlumnoAccesoDatos:
    def __init__(self):
        pass


    def listar_todos_alumnos(self) -> List[Alumno]:
        """
        Este método devuelve una lista con todos los alumnos.

        Este método se encarga de devolver una lista de python con los objetos del modelo de los alumnos disponibles en la base de datos.
        Los objetos de tipo Alumno serán basados en la clase Alumno.

        Parameters:
        None

        Returns:
        List[Alumno]: Lista con todos los alumnos disponibles
        """
        return Alumno.query.all()
