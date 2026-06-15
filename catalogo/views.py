
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto

# Creación de la vista de catalogo

# Vista privada del catalogo
@login_required
def catalogo_view(request):
    productos = Producto.objects.all()

    return render(request, 'catalogo/index.html', {
        'productos': productos
    })
    
