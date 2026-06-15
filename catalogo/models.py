from django.db import models

# Create your models here.

# Tabla proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    tipo_producto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    


# Tabla categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre



# Tabla producto
class Producto(models.Model):
    codigo = models.CharField(max_length=30, unique=True, blank=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete= models.CASCADE,
        related_name='productos'
    )

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete= models.CASCADE,
        related_name='productos',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre





