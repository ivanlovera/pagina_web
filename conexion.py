from flask import Flask
from models import db

#se crea una instancia de la aplicacion Flask

app = Flask(__name__)

#Configurar la URL de la base de datos

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datos_usuarios.db"

#Inicializamos la extension SQLALCHEMY en la aplicacion Flask

db.init_app(app)


#Con esto se asegura que las operaciones con la base de datos se realicen correctamente 
with app.app_context():
    db.create_all()

