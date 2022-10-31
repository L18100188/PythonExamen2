from django.urls import path, include
from . import views

urlpatterns = [
    #peliculas
    path('pelicula/insert', views.pelicula_form, name='pelicula_insert'), 
    path('pelicula/<int:id>', views.pelicula_form, name='pelicula_update'), 
    path('pelicula/delete/<int:id>',views.pelicula_delete, name='pelicula_delete'),
    path('pelicula/lista/', views.pelicula_list, name='pelicula_list'),
    path('', views.homepage, name='homepage'),
    #Videojuegos
    path('videojuego/insert', views.videojuego_form, name='videojuego_insert'), 
    path('videojuego/<int:id>', views.videojuego_form, name='videojuego_update'), 
    path('videojuego/delete/<int:id>',views.videojuego_delete, name='videojuego_delete'),
    path('videojuego/lista/', views.videojuego_list, name='videojuego_list'),
    #serie
    path('serie/insert', views.serie_form, name='serie_insert'), 
    path('serie/<int:id>', views.serie_form, name='serie_update'), 
    path('serie/delete/<int:id>',views.serie_delete, name='serie_delete'),
    path('serie/lista/', views.serie_list, name='serie_list')
]