from django.db import models
from catalogo.models import Producto
from clientes.models import Cliente

# Modelos según el módulo de pedidos  

# Tabla pedido
class Pedido(models.Model):

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )

    fecha = models.DateTimeField(auto_now_add=True)
    
    TIPO_ESTADO = [
        ("Pendiente", "Pendiente"),
        ("Cancelado", "Cancelado"),
        ("Pagado", "Pagado"),
        ("Enviado", "Enviado"),
        ("Entregado", "Entregado"),
    ]

    estado = models.CharField(max_length=20, choices=TIPO_ESTADO)

    # Se calcula dinámicamente a partir de todos los detalles del pedido.
    @property
    def total(self):
        return sum(
            detalle.cantidad * detalle.precio_unitario
            for detalle in self.detalles.all()
        )

    def __str__(self):
        return f"Pedido #{self.id}"



# Tabla intermedia (Detalle_pedido)
class Detalle_pedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='detalles'
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='detalles'
    )

    cantidad = models.PositiveBigIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario
    

    def save(self, *args, **kwargs):
        self.precio_unitario = self.producto.precio
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detalle {self.id} - {self.pedido.cliente}"

    # Agregación de constraint para evitar duplicaciones
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pedido', 'producto'],
                name='unique_producto_por_pedido'
            )
        ]




