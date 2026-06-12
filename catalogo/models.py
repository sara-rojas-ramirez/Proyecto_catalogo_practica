from django.db import models

# Create your models here.

# Tabla cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

# Tabla proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    tipo_producto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    


# Tabla categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre



# Tabla producto
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete= models.CASCADE,
        related_name='productos'
    )

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete= models.CASCADE,
        related_name='productos'
    )

    def __str__(self):
        return self.nombre



# Tabla pedido
class Pedido(models.Model):
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    TIPO_ESTADO = {
        "Pendiente": "Pendiente",
        "Cancelado": "Cancelado",
        "Pagado": "Pagado",
        "Enviado": "Enviado",
        "Entregado": "Entregado"
    }

    estado = models.CharField(max_length=1, choices=TIPO_ESTADO)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='Pedidos'
    )

    def __str__(self):
        return f"Pedido #{self.id}"


# Tabla intermedia (Detalle_pedido)
class Detalle_pedido(models.Model):
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

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

    def __str__(self):
        return f"Detalle {self.id}"

