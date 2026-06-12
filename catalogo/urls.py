# Se creo un archivo URLS principal para cada una de las rutas de la aplicación catalogo, esto evita tener que colocar muchas rutas en las urls.py del proyecto principal

from django.urls import path
from . import views

urlpatterns = [
    path('catalogo', views.saludar)
]