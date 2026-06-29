# URLS propias del modulo

from django.urls import path
from . import views


urlpatterns = [
    path("", views.ver_carrito, name="ver_carrito"),
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar_producto"),
    path("eliminar/<int:item_id>/", views.eliminar_producto, name="eliminar_producto"),
    path("actualizar/<int:item_id>/", views.actualizar_carrito, name="actualizar_carrito"),
    path("vaciar/", views.vaciar_carrito, name="vaciar_carrito")
]
