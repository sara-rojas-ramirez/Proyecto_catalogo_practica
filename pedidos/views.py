from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pedido



# Aqui va lista pedidos, detalle pedido, cancelar pedido y actualizar estado

# Vista de detalle del pedido
@login_required
def detalle_pedido(request, pedido_id):
    # Usamos select_related para traer los datos geográficos de una sola vez
    pedido = get_object_or_404(
        Pedido.objects.select_related('checkout__departamento', 'checkout__municipio', 'checkout__barrio'),
        id=pedido_id,
        cliente=request.user.cliente
    )

    detalles = pedido.detalles.all()

    return render(request, "pedido/detalle_pedido.html", {
        "pedido": pedido,
        "detalles": detalles
    })








