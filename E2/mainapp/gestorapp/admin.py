from django.contrib import admin
from .models import Serie, Pelicula, Plataforma, Videojuego, Clasificacion

# Register your models here.
admin.site.register(Serie)
admin.site.register(Pelicula)
admin.site.register(Plataforma)
admin.site.register(Videojuego)
admin.site.register(Clasificacion)