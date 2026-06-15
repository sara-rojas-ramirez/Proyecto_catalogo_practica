from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalogo.models import Producto
from .models import Carrito, Item_carrito
from pedidos.models import Pedido, Detalle_pedido


# Vista y funcionalidad para ver carrito
@login_required
def ver_carrito(request):
    cliente = request.user.cliente

    carrito, created = Carrito.objects.get_or_create(
        cliente = cliente,
        defaults={"activo": True}
    )

    items = carrito.item_carrito_set.all()
    total = sum(
        item.cantidad * item.producto.precio
        for item in items
    )

    return render(request, "carrito/ver_carrito.html", {
        "carrito": carrito,
        "items": items,
        "total": total
    })



# Vista y funcionalidad de agregar producto
@login_required
def agregar_producto(request, producto_id):
    if request.method != "POST":
        return redirect("catalogo")

    cliente = request.user.cliente

    carrito, created = Carrito.objects.get_or_create(
        cliente = cliente,
        defaults={"activo": True}
    )

    producto = get_object_or_404(Producto, id = producto_id)

    item, created = Item_carrito.objects.get_or_create(
        carrito = carrito,
        producto = producto
    )

    if not created:
        item.cantidad += 1
        item.save()
    
    return redirect("ver_carrito")



# Vista y funcionalidad de eliminar item
@login_required
def eliminar_producto(request, item_id):
    cliente = request.user.cliente
    carrito = get_object_or_404(Carrito, cliente=cliente)

    item = get_object_or_404(
        Item_carrito,
        id=item_id,
        carrito=carrito
    )

    item.delete()
    return redirect("ver_carrito")


# Falta actualizar cantidad 
@login_required
def actualizar_carrito(request, item_id):
    cliente = request.user.cliente
    carrito = get_object_or_404(Carrito, cliente=cliente)
    
    item = get_object_or_404(Item_carrito, id=item_id, carrito=carrito)

    if request.method == "POST":
        cantidad = int(request.POST.get("cantidad", 1))

        if cantidad > 0:
            item.cantidad = cantidad
            item.save()
        else:
            item.delete()

    return redirect("ver_carrito")



# Funcionalidad de vaciar carrito
@login_required
def vaciar_carrito(request):
    cliente = request.user.cliente
    carrito = get_object_or_404(Carrito, cliente=cliente)

    carrito.item_carrito_set.all().delete()

    return redirect("ver_carrito")



# Funcionalidad checkout
@login_required
def checkout(request):
    cliente = request.user.cliente
    carrito = get_object_or_404(Carrito, cliente = cliente)

    items = carrito.item_carrito_set.all()

    if not items.exists():
        return redirect("ver_carrito")
    
    pedido = Pedido.objects.create(
        cliente = cliente,
        estado = "Pendiente"
    )

    for item in items:
        Detalle_pedido.objects.create(
            pedido = pedido,
            producto = item.producto,
            cantidad = item.cantidad,
            precio_unitario = item.producto.precio
        )
    
    items.delete()

    return redirect("ver_carrito")



