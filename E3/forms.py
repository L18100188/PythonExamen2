from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CancionForm(FlaskForm):
    nombreCancion=StringField("Cancion", validators=[DataRequired()])# es un dato que debe ser requerido
    fechaEstreno = StringField("Fecha de lanzamiento")
    discografica=StringField("discografica")
    duracion = StringField("Duracion")
    enviar = SubmitField("Enviar")

class AlbumForm(FlaskForm):
    nombreAlbum=StringField("Album", validators=[DataRequired()])# es un dato que debe ser requerido
    fechaLanzamiento = StringField("Lanzamiento")
    discografica=StringField("discografica")
    numCanciones = StringField("Canciones que contiene el disco")
    enviar = SubmitField("Enviar")
