from flask_restful import Resource
from flask import Flask, request
from app.controller.AlumnoController import *

class Listar_alumnos(Resource):
    def post(self):
        data = request.get_json()
        # VERIFICACION
        # SEGURIDAD
        rpta = listarAlumnos()
        
        return rpta 