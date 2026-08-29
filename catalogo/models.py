from django.db import models

# Tabla proveedor
# Representa a los proveedores y cada uno tiene restricciones de unicidad en su nombre y correo.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    tipo_producto = models.CharField(max_length=50)

    # Permite ver el nombre real en el panel del admin
    def __str__(self):
        return self.nombre
    


# Tabla categoria
# Agrupa los productos en secciones
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre



# Tabla producto
# Es laa entidad principal del catalogo, almacena la información del articulo y se conecta con categoria y proveedor.
class Producto(models.Model):
    codigo = models.CharField(max_length=30, unique=True, blank=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    imagen = models.ImageField(upload_to='productos/', null = True, blank = True)

    # Estas son las relaciones (claves foraneas)
    categoria = models.ForeignKey(
        Categoria,
        # Si se borra la categoria, se borran sus productos
        on_delete= models.CASCADE,
        # Permite hacer: categoria.productos.all()
        related_name='productos'
    )

    proveedor = models.ForeignKey(
        Proveedor,
        # Lo mismo, si se borra el proveedor, se borran sus productos
        on_delete= models.CASCADE,
        # Permiten hacer: proveedor.productos.all()
        related_name='productos',
        # Permite que un producto se quede temporalmente sin proveedores
        null=True,
        # Permite dejar el campo vacio en formularios
        blank=True
    )

    def __str__(self):
        return self.nombre





