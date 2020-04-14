from dataclasses import dataclass
from typing import Dict

@dataclass
class AlumnoDTO:
    id_alumno: int = None
    nombre: str = None
    apellido: str = None

    def toJson(self) -> Dict:
        return {
            'id_alumno': self.id_alumno,
            'nombre': self.nombre,
            'apellido': self.apellido
        }
