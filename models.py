from flask_sqlalchemy import SQLAlchemy

#inicializar la extension de la aplicacion flask

db = SQLAlchemy()

#definimos una clase que representa una tabla en la base de datos 

class Usuarios(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nombre  =  db.Column(db.String[20], nullable = False)
    apellido = db.Column(db.String[20], nullable = False)
    correo = db.Column(db.String[20], nullable = False)

    #Constructor de clase
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

        


class Textos(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    texto_largo = db.Column(db.String[300], nullable = True)

    #Constructor de clase
    def __init__(self, texto_largo):
        self.texto_largo = texto_largo


