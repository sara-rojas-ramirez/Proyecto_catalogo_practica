
from django.urls import path
from . import views

urlpatterns = [
     path('formsCheckout/', views.checkout_view, name = 'formsCheckout'),

     # Rutas AJAX para la cascada
     path('ajax/cargar-municipios/', views.cargar_municipios, name='ajax_cargar_municipios'),
     path('ajax/cargar-barrios/', views.cargar_barrios, name='ajax_cargar_barrios')
]

 
