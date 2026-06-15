# Definir las URLS del módulo accounts
# Deben de conectarse estas urls con elas ulrs principales

from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.login_view, name = 'login'),
     path('logout/', views.logout_view, name = 'logout')
]




