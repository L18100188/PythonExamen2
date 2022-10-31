from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CineForm(FlaskForm):
    nombreCine=StringField("Nombre Cine", validators=[DataRequired()])# es un dato que debe ser requerido
    direccion= StringField("Direccion")
    numSalas=StringField("Numero de salas")
    horario = StringField("Horario")
    enviar = SubmitField("Enviar")

class SalaCinesForm(FlaskForm):
    capacidad=StringField("Capacidad", validators=[DataRequired()])# es un dato que debe ser requerido
    ocupado = StringField("Ocupacion de la sala")
    horaProxFuncion=StringField("Funcion proxima")
    enviar = SubmitField("Enviar")
