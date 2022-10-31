from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import PeliculaForm, VideojuegoForm, SerieForm
from .models import Pelicula, Videojuego, Serie

# Create your views here.
def pelicula_list(request):
    context = {'pelicula_list': Pelicula.objects.all()}
    return render(request, "pelicula/pelicula_list.html", context)

def pelicula_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PeliculaForm()
        else:
            pelicula = Pelicula.objects.get(pk=id)
            form = PeliculaForm(instance=pelicula)

        return render(request, "pelicula/pelicula_form.html",{'form':form})
    else:
        if id == 0: 
            form = PeliculaForm(request.POST)
        else:
            pelicula = Pelicula.objects.get(pk=id)
            form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
        return redirect('/pelicula/lista')

def pelicula_delete(request, id):
    pelicula = Pelicula.objects.get(pk=id)
    pelicula.delete()
    return redirect('/pelicula/lista')

#Videojuego
def videojuego_list(request):
    context = {'videojuego_list': Videojuego.objects.all()}
    return render(request, "videojuego/videojuego_list.html", context)

def videojuego_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = VideojuegoForm()
        else:
            videojuego = Videojuego.objects.get(pk=id)
            form = VideojuegoForm(instance=videojuego)

        return render(request, "videojuego/videojuego_form.html",{'form':form})
    else:
        if id == 0: 
            form = VideojuegoForm(request.POST)
        else:
            videojuego  = Videojuego.objects.get(pk=id)
            form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
        return redirect('/videojuego/lista')

def videojuego_delete(request, id):
    videojuego = Videojuego.objects.get(pk=id)
    videojuego.delete()
    return redirect('/videojuego/lista')

#Serie
def serie_list(request):
    context = {'serie_list': Serie.objects.all()}
    return render(request, "serie/serie_list.html", context)

def serie_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = SerieForm()
        else:
            serie = Serie.objects.get(pk=id)
            form = SerieForm(instance=serie)

        return render(request, "serie/serie_form.html",{'form':form})
    else:
        if id == 0: 
            form = SerieForm(request.POST)
        else:
            serie  = Serie.objects.get(pk=id)
            form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
        return redirect('/serie/lista')

def serie_delete(request, id):
    serie = Serie.objects.get(pk=id)
    serie.delete()
    return redirect('/serie/lista')

def homepage(request):
    return render(request, "pelicula/homepage.html")