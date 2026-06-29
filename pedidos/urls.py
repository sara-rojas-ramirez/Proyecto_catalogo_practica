from django.urls import path
from . import views

urlpatterns = [
    path("detalle/<int:pedido_id>/", views.detalle_pedido, name = "detalle_pedido")
]


