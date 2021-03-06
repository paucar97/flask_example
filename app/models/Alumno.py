from . import db


class Alumno(db.Model):
    __tablename__ = "ALUMNO_DB"
    #mejor llamo
    id_alumno = db.Column('ID_ALUMNO',db.Integer,primary_key=True)
    nombre = db.Column('NOMBRE', db.String(50), nullable=False)
    apellido_paterno = db.Column('APELLIDO_PATERNO', db.String(100))
    
    def toJson(self):
        d= {}
        d['id_alumno'] = self.id_alumno
        d['nombre'] = self.nombre
        d['apellido_paterno'] = self.apellido_paterno
        return d

    @classmethod
    def getAll(self):
        return Alumno.query.all() # select * from alumno

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_alumno

    @classmethod
    def getOne(self,id):
        alumno = Alumno.query.filter_by(id_alumno = id).first()
        return alumno
