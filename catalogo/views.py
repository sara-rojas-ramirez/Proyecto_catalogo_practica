
# Importaciones:
# get_objet_or_404: busca un objeto en la bd, si no existe, muestra error 404 (pagina no encontrada)
# login_required: decorador que obliga al usuario a estar logueado
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Categoria


# catalogo_view: muestra la pagina principal del catalogo 
@login_required
def catalogo_view(request):
    # Obtiene la categoria desde el URL
    # por ejemplo: /catalogo/?categoria=2, entonces eso significa que obtiene la categoria donde su id es 2.
    categoria_id = request.GET.get('categoria')

    # Obtiene todos los productos, es equivalente a SELECT * FROM producto; lo mismo para categoria.
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    # Filtra por la categoria y muestra los productos de esa categoria usando filter 
    if categoria_id:
        productos = productos.filter(categoria_id = categoria_id)

    # Renderiza HTML
    return render(request, 'catalogo/home.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_activa': categoria_id
    })



# Vista_agrandada_view: muestra un producto individual en grande
@login_required
# Recibe la solicitud y el id del producto que se selecciono
def vista_agradanda_view(request, producto_id):
    # Se busca el producto por su ID, si no existe arroja error 404
    producto = get_object_or_404(Producto, id = producto_id)

    # Renderiza la vista agrandada y manda el producto al HTML
    return render(request, 'catalogo/vista_agrandada.html', {
        'producto': producto
    })


    
