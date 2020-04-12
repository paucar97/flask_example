from flask_restful import Resource
from flask import Flask, request
from app.controller.AlumnoController import *
from app.dto.AlumnoDTO import AlumnoDTO

class Listar_alumnos(Resource):
    def post(self):
        data = request.get_json()
        # VERIFICACION
        # SEGURIDAD
        rpta = listarAlumnos()
        
        return jsonify(code=200, data=rpta.toJson(), message='Alumnos obtenidos con exito')

class Crear_alumno(Resource):
    def post(self):
        data = request.get_json()
        alumnoDTO = AlumnoDTO(id_alumno=None, nombre=data['nombre'], apellido=data['apellido'])
        return crearAlumno(alumnoDTO)

class Obtener_alumno(Resource):
    def post(self):
        data = request.get_json()
        idAlumno = data['idAlumno']
        return obtenerAlumno(idAlumno)
