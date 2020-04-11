from . import db
from app.models.Curso import Curso
from app.models.Alumno import Alumno

class Alumno_Curso(db.Model):
    __tablename__ = 'ALUMNO_X_CURSO_DB'
    id_curso= db.Column('ID_CURSO',db.ForeignKey(Curso.id_Curso),primary_key=True)
    id_alumno = db.Column('ID_ALUMNO',db.ForeignKey(Alumno.id_alumno),primary_key=True)
    
