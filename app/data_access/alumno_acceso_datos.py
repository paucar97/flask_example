from app.models import db
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

    def agregar_un_alumno(self, alumno: Alumno) -> Alumno:
        """
        Este método agrega un alumno a la base de datos

        Parameters:
        alumno (Alumno): Alumno a ser agregado

        Returns:
        Alumno: El alumno agregado
        """
        db.session.add(alumno)
        db.session.flush()
        db.session.commit()
        return alumno

    def obtener_alumno_por_id(self, id_alumno: int) -> Alumno:
        """
        Este método devuelve un alumno cuando es buscado por su id
        
        Parameters:
        id_alumno (int): El id del alumno a buscar

        Returns:
        Alumno: El alumno encontrado
        """
        return Alumno.query.filter_by(id_alumno = id_alumno).first()