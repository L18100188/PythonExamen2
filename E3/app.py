from flask import Flask,render_template,request,redirect,url_for,jsonify
from database import db
from flask_migrate import Migrate

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