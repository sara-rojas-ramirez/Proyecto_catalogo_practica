# Definir las URLS del módulo accounts
# Deben de conectarse estas urls con elas ulrs principales

from django.urls import path
from . import views
from clientes.views import registroView
from django.contrib import admin

urlpatterns = [
     path('login/', views.login_view, name = 'login'),
     path('logout/', views.logout_view, name = 'logout'),
     path('registro/', registroView, name = 'registro'),
     # path('admin/', admin.site.urls, name = 'admin'),

     # Rutas ajax
     path('ajax/login/', views.login_ajax, name = 'ajax_login')
]




