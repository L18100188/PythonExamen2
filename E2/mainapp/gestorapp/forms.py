from django import forms
from .models import Pelicula, Videojuego, Serie

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula
        fields = '__all__'
        labels = {
            'titulo': 'Titulo',
            'codigo': 'Codigo',
            'genero': 'Genero',
            'clasificacion': 'Clasificacion'
        }
        
    def __init__(self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        self.fields['clasificacion'].empty_label = "-- Seleccionar --"

class VideojuegoForm(forms.ModelForm):

    class Meta:
        model = Videojuego
        fields = '__all__'
        labels = {
            'titulo': 'Titulo',
            'codigo': 'Codigo',
            'calificacion': 'Calificacion',
            'plataforma': 'Plataforma'
        }
        
    def __init__(self, *args, **kwargs):
        super(VideojuegoForm, self).__init__(*args, **kwargs)
        self.fields['plataforma'].empty_label = "-- Seleccionar --"

class SerieForm(forms.ModelForm):

    class Meta:
        model = Serie
        fields = '__all__'
        labels = {
            'titulo': 'Titulo',
            'codigo': 'Codigo',
            'capitulos': 'Capitulos',
            'calificacion': 'Calificacion'
        }
