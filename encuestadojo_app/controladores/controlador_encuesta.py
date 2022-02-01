from flask import render_template, request, redirect, session
from encuestadojo_app import app
from encuestadojo_app.modelos.modelo_encuesta import Encuesta

@app.route('/' , methods=['GET'])
def paginaPrincipal():
     return render_template('index.html')

@app.route('/result',methods=['GET'])
def paginaRegistro():
     comentario=Encuesta.visualiza()
     print("hola",comentario)
     return render_template('plataforma.html',datos=comentario[0])
 

@app.route('/registro', methods=['POST'])
def Registro():
    nuevaEncuesta={
        "nombre" : request.form["nombre"],
        "lugar" : request.form["lugar"],
        "lenguaje" : request.form["lenguaje"],
        "comentario" : request.form["comentario"]
    }
    validar=Encuesta.Validacion(nuevaEncuesta)
    if validar == True :
        resultado=Encuesta.agregarDojo(nuevaEncuesta) 
        return redirect('/result')
    else:
         return redirect('/')

@app.route('/salir', methods=['GET'])
def Salir():
    session.clear()
    return redirect('/')