
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Categoria

# Creación de la vista de catalogo

# Vista privada del catalogo
@login_required
def catalogo_view(request):
    categoria_id = request.GET.get('categoria')

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    if categoria_id:
        productos = productos.filter(categoria_id = categoria_id)

    return render(request, 'catalogo/home.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_activa': categoria_id
    })


# Vista agrandada del producto
@login_required
def vista_agradanda_view(request, producto_id):
    # Se busca el producto por su ID, si no existe arroja error 404
    producto = get_object_or_404(Producto, id = producto_id)

    return render(request, 'catalogo/vista_agrandada.html', {
        'producto': producto
    })


    
