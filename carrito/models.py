from django.db import models
from clientes.models import Cliente
from catalogo.models import Producto


# Carrito (Representa el carrito actual del cliente, con una relación de 1 a 1 con el cliente, porque el cliente solo puede tener un carrito)
class Carrito(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)


# Items del carrito (Porque un carrito tiene varios productos, entonces recibe id carrito, id producto y cantidad)
class Item_carrito(models.Model):

    carrito = models.ForeignKey(
        Carrito,
        on_delete=models.CASCADE
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )
    cantidad = models.PositiveBigIntegerField(default = 1)

    @property
    def subtotal(self):
        return self.cantidad * self.producto.precio
