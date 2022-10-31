from flask import Flask,render_template, redirect, url_for,jsonify,request
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

@app.route('/verCine/<int:id>')
def verDetalleCine(id):
    cine=Cine.query.get_or_404(id)
    return render_template('detalleCine.html',cine=cine)

@app.route('/agregarCine', methods=["GET","POST"])
def agregarCine():
    cine = Cine()
    cineForm=CineForm(obj=cine)
    if request.method=="POST":
        if cineForm.validate_on_submit():
            cineForm.populate_obj(cine)
            db.session.add(cine)
            db.session.commit()
            return redirect(url_for('mostrarCine'))
    return render_template('agregarCine.html', forma=cineForm)


#Entidad Salas de cine -----------------------------------------------------------------------
@app.route('/Sala')
def mostrarSala():
    salasCine= SalaCine.query.all()
    return render_template('Sala.html', salasCine=salasCine)

@app.route('/verSala/<int:id>')
def verDetalleSala(id):
    salaCine=SalaCine.query.get_or_404(id)
    return render_template('detalleSala.html',salaCine=salaCine)

@app.route('/agregarSala', methods=["GET","POST"])
def agregarSala():
    sala= SalaCine()
    salaForm=SalaCinesForm(obj=sala)
    if request.method=="POST":
        if salaForm.validate_on_submit():
            salaForm.populate_obj(sala)
            #insertar a la base de datos
            db.session.add(sala)
            db.session.commit()
            return redirect(url_for('mostrarSala'))
    return render_template('agregarSala.html',forma=salaForm)


@app.route('/editarSala/<int:idSala>',methods=['GET','POST'])
def editarSala(idSala):
    sala=SalaCine.query.get_or_404(idSala)
    salaForm=SalaCinesForm(obj=sala)
    if request.method == "POST":
        if salaForm.validate_on_submit():
            salaForm.populate_obj(sala)
            db.session.commit()
            return redirect(url_for('mostrarSala'))
    return render_template('editarSala.html', forma=salaForm)