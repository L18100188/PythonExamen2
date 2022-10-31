from django.db import models

# Create your models here.
class Clasificacion(models.Model):
    titulo_cla = models.CharField(max_length=3)

    def __str__(self):
        return self.titulo_cla

class Plataforma(models.Model):
    titulo_pla = models.CharField(max_length=3)

    def __str__(self):
        return self.titulo_pla


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=30)
    genero = models.CharField(max_length=50)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=30)
    calificacion = models.CharField(max_length=3)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=30)
    capitulos = models.CharField(max_length=5)
    calificacion = models.CharField(max_length=5)

    def __str__(self):
        return self.titulo