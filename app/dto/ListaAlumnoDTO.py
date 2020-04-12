from dataclasses import dataclass
from typing import List, Dict
from app.models.Alumno import Alumno


@dataclass
class ListaAlumnoDTO:
    lista_alumnos: List[Alumno]
    cant_alumnos: int

    def toJson(self) -> Dict:
        return {
            'lista_alumnos': [alumno.toJson() for alumno in self.lista_alumnos],
            'cant_alumnos': self.cant_alumnos
        }