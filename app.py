from conexion import app, db
from models import Usuarios, Textos
from flask import render_template, request, url_for, redirect


@app.route('/', methods = ['POST', 'GET'])

def cargar_datos():
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']

        #Creamos un objeto de la clase Usuarios con los datos obtenidos
        datos_usuarios = Usuarios(nombre, apellido, correo)
        db.session.add(datos_usuarios)
        db.session.commit()
        return redirect(url_for("cargar_textos",usuario_id = datos_usuarios.id))
    return render_template('index.html')

@app.route('/cargar_textos', methods = ['GET', 'POST'])

def cargar_textos():
    if request.method == 'POST':
        texto_largo = request.form['texto_largo']
        
        texto = Textos(texto_largo)  #objeto de la clase Textos 
        texto_id = texto.id   #se obtiene su id para enviarlo luego al html
        db.session.add(texto)
        db.session.commit()
        return redirect(url_for("mostrar_texto.html",texto_id=texto_id))
    return render_template("cargar_textos.html")
  


#Ruta para mostrar los registros cargados en la base de datos 
@app.route('/mostrar_datos', methods = ['POST', 'GET'])
def mostrar_datos():
    lista_usuarios = Usuarios.query.all()
    return render_template('mostrar_datos.html', lista_usuarios = lista_usuarios)




#######  ACTUALIZAR ########

@app.route('/actualizar/<int:usuario_id>', methods =  ['GET', 'POST'])
def actualizar(usuario_id):
    usuario_a_actualizar = Usuarios.query.get(usuario_id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']

        usuario_a_actualizar.nombre = nombre
        usuario_a_actualizar.apellido = apellido
        usuario_a_actualizar.correo = correo
        

        db.session.commit()


        return redirect(url_for('mostrar_datos'))
    
    return render_template("actualizar.html", usuario_a_actualizar = usuario_a_actualizar)





@app.route('/mostrar_texto/<int:texto_id>', methods = ['GET', 'POST'])

def mostrar_texto(texto_id):
    texto = Textos.query.get(texto_id)
    return render_template('mostrar_texto.html', texto)
   


####### ELIMINAR ########


@app.route('/eliminar', methods = ['GET','POST'])
def eliminar():
    if request.method == 'POST':
        id = request.form['usuario_id']
        usuario_a_eliminar = Usuarios.query.filter_by(id=id).first()

        db.session.delete(usuario_a_eliminar)
        db.session.commit()

        return redirect(url_for('mostrar_datos'))



if __name__== "__main__":
    app.run(debug=True)