
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('catalogo', include('catalogo.urls')),
    path('carrito/', include("carrito.urls")),
    path('checkout/', include("checkout.urls")),
    path('pedidos/', include('pedidos.urls')),
    path('gestion/', include('gestion_admin.urls'))
]

# Esto permite que django sirva las imagenes mientras se desarrolla
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)