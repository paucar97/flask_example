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

class Crear_alumno(Resource):
    def post(self):
        data = request.get_json()
        nombreAlumno = data['nombre']
        apellidoAlumno = data['apellido']
        return crearAlumno(nombreAlumno,apellidoAlumno)

class Obtener_alumno(Resource):
    def post(self):
        data = request.get_json()
        idAlumno = data['idAlumno']
        return obtenerAlumno(idAlumno)
