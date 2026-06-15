from django.contrib import admin
from .models import Pedido, Detalle_pedido

# Register your models here.

admin.site.register(Pedido)
admin.site.register(Detalle_pedido)
