from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalogo.models import Producto
from .models import Pedido, Detalle_pedido
from carrito.models import Carrito, Item_carrito
from clientes.models import Cliente

# aqui va lista pedidos, detalle pedido, cancelar pedido y actualizar estado







