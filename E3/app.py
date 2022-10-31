from flask import Flask,render_template,request,redirect,url_for,jsonify
from database import db
from flask_migrate import Migrate
from models import Cine,SalaCine,Pelicula,Producto,Boleto
from forms import CineForm,SalaCinesForm

#Aplicacion
app=Flask(__name__)

#Configuracion de la base de datos
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB ='db_cine'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI']= FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)

#configurar migracion
migrate=Migrate()
migrate.init_app(app,db)

#form
app.config["SECRET_KEY"]="una llave muy secreta"
# app.secret_key="llave_secreta"

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html',error=error), 404

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    return render_template('index.html')

#Entidad Cine-----------------------------------------------------------------
@app.route('/cine')
def mostrarCine():
    cines=Cine.query.all()
    return render_template('cine.html',cines=cines)

@app.route('/verCancion/<int:id>')
def verDetalleCancion(id):
    cine=Cine.query.get_or_404(id)
    return render_template('detalleCine.html',cine=cine)

@app.route('/agregarCine', methods=["GET","POST"])
def agregarCine():
    cine = Cine()
    cineForm=CineForm(obj=cine)
    if request.method=="POST":
        if cineForm.validate_on_submit():
            cineForm.populate_obj(cine)
            #insertar a la base de datos
            db.session.add(cine)
            db.session.commit()
            return redirect(url_for('mostrarCine'))
    return render_template('agregarCine.html',forma=cineForm)