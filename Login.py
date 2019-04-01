from flask import Flask, render_template
from flask_wtf import FlaskForm

app = Flask(__name__)

app.config ['Contraseña'] = 'Estaeslacontraseña'

@app.route('/inicio')
def index():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def i():
    return "Listo"

@app.route('/usuarios_agregados')
def usuarios_agregados():
    return "Mi pagina de usuarios"
    
    l=[]
    Usuario1 ={ "Nombre" "apellido" "edad":}
    Usuario2 ={ "Nombre" "apellido" "edad":}
    Usuario3 ={ "Nombre" "apellido" "edad":}
    Usuario4 ={ "Nombre" "apellido" "edad":}
    Usuario5 ={ "Nombre" "apellido" "edad":}
    Usuario6 ={ "Nombre" "apellido" "edad":}
    Usuario7 ={ "Nombre" "apellido" "edad":}
    Usuario8 ={ "Nombre" "apellido" "edad":}
    Usuario9 ={ "Nombre" "apellido" "edad":}

    l.append(Usuario1)
    l.append(Usuario2)
    l.append(Usurio3)
    l.append(Usuario4)
    l.append(Usuario5)
    l.append(Usuario6)
    l.append(Usuario7)
    l.append(Usuario8)
    l.append(Usuario9)
    l.append(Usuario10)

    return render_template('inicio.html',l=l)

@app.route('/editar_usarios')
def editar_usarios():
    return 'editar usuarios'

@app.route('/eliminar_usarios')
def eliminar_usarios():
    return 'eliminar usuarios'


@app.route('/usuarios/<id>')
def usario(id):
   
    return "Mi usuario es:" + str(id)

app.run (debug=True)