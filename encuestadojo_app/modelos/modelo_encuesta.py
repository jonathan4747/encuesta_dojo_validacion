from encuestadojo_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Encuesta:
    
    def __init__(self,id,nombre,lugar,lenguaje,comentario,created_at,updated_at):
        self.id = id
        self.name=nombre
        self.name=lugar
        self.name=lenguaje
        self.name=comentario
        self.created_at=created_at
        self.updated_at=updated_at
        
    @classmethod
    def agregarDojo(cls,nuevo):
        query = "INSERT INTO dojos(nombre,lugar,lenguaje,comentario,created_at,updated_at) VALUES(%(nombre)s,%(lugar)s,%(lenguaje)s,%(comentario)s,NOW(),NOW());"
        resultado = connectToMySQL("encuesta_dojo").query_db(query,nuevo)
        return resultado

    @classmethod
    def visualiza(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        resultado = connectToMySQL("encuesta_dojo").query_db(query)
        print("que es",resultado)
        return resultado
    
    @staticmethod
    def Validacion(nuevo):
        valida= True
        if len(nuevo['nombre']) <= 2:
            valida = False
            flash("El nombre no debe tener menos que 2 caracteres")
        if len(nuevo['lugar']) < 1:
            valida= False
            flash("Escoge un lugar")
        if len(nuevo['lenguaje']) < 1:
            valida = False
            flash("Escoger un lenguaje del menu")
        return valida