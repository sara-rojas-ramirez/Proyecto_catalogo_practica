from django.contrib import admin
from .models import Proveedor, Categoria, Producto 

# Registrar los modelos en el admin

admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)