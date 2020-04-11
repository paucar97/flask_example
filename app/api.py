from flask_restful import Api
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from app.models import db
from app.models.Alumno import Alumno
from app.models.Curso import Curso
from app.models.Alumnos_Curso import Alumno_Curso

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.resource.AlumnoResource import *

api.add_resource(Listar_alumnos, '/api/listar_alumnos')