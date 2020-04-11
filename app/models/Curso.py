from . import db

class Curso(db.Model):
    __tablename__ = "CURSO_DB"
    id_Curso = db.Column('ID_CURSO',db.Integer,primary_key=True)
    nombre = db.Column('NOMBRE_CURSO', db.String(50), nullable=False)
    cred = db.Column('CREDITO',db.Float)