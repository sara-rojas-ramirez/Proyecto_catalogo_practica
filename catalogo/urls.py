# Se creo un archivo URLS principal para cada una de las rutas de la aplicación catalogo, esto evita tener que colocar muchas rutas en las urls.py del proyecto principal

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.catalogo_view, name='catalogo'),
    path('vista-agrandada/<int:producto_id>/', views.vista_agradanda_view, name = "vista_agrandada")
]