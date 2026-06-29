from django.contrib import admin
from . models import Checkout, Pago, Departamento, Municipio, Barrio

# Register your models here.
admin.site.register(Checkout)
admin.site.register(Pago)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Barrio)