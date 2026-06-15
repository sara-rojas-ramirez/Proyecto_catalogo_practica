
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('catalogo', include('catalogo.urls')),
    path('carrito/', include("carrito.urls"))
]
