# Importamos el módulo models de Django, que permite crear tablas en la base de datos
# usando clases de Python (ORM).
from django.db import models

# Importamos el modelo Cliente desde la app clientes.
# Esto permite relacionar el checkout con el cliente que realiza la compra.
from clientes.models import Cliente


# Es importante separar checkout y pago:
# - Checkout: guarda la información logística de la compra (dirección, ubicación, cliente).
# - Pago: guarda la información financiera (método, estado, referencia).
# Esta separación mejora la organización y escalabilidad del sistema.



# =========================
# MODELOS GEOGRÁFICOS
# =========================

# Este modelo representa un departamento (ej: Risaralda, Antioquia, Valle del Cauca).
# Se usa para estructurar la dirección de envío jerárquicamente.
class Departamento(models.Model):

    # Campo de texto para almacenar el nombre del departamento.
    # unique=True evita que se repita el mismo nombre.
    nombre = models.CharField(max_length=50, unique=True)

    # Define cómo se mostrará el objeto en el panel admin o en consultas.
    def __str__(self):
        return self.nombre
    


# Este modelo representa un municipio que pertenece a un departamento.
# Ejemplo: Pereira pertenece a Risaralda.
class Municipio(models.Model):

    # Relación muchos-a-uno:
    # Un departamento puede tener muchos municipios.
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        related_name='municipios'
    )

    # Nombre del municipio
    nombre = models.CharField(max_length=50)

    # Restricción para evitar municipios duplicados dentro del mismo departamento.
    # Ejemplo:
    # ✔ Pereira en Risaralda
    # ✔ Pereira en otro departamento (si existiera)
    # ✖ Pereira repetido dos veces en Risaralda
    class Meta:
        unique_together = ('departamento', 'nombre')

    # Representación legible del municipio.
    def __str__(self):
        return f"{self.nombre} ({self.departamento.nombre})"



# Este modelo representa un barrio dentro de un municipio.
# Ejemplo: Cuba pertenece a Pereira.
class Barrio(models.Model):

    # Un municipio puede tener muchos barrios.
    municipio = models.ForeignKey(
        Municipio,
        on_delete=models.CASCADE,
        related_name='barrios'
    )

    # Nombre del barrio
    nombre = models.CharField(max_length=50)

    # Representación legible
    def __str__(self):
        return self.nombre



# =========================
# MODELO CHECKOUT
# =========================

# Este modelo representa el proceso de checkout:
# cuando el usuario confirma la compra y registra su dirección de entrega.
class Checkout(models.Model):

    # Relación con el cliente que realiza la compra.
    # Un cliente puede tener muchos checkouts a lo largo del tiempo.
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )

    # Departamento seleccionado para la entrega.
    # PROTECT evita eliminar el departamento si está siendo usado en un checkout.
    # null=True y blank=True permiten dejarlo vacío temporalmente.
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    # Municipio seleccionado para la entrega.
    municipio = models.ForeignKey(
        Municipio,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    # Barrio seleccionado para la entrega.
    barrio = models.ForeignKey(
        Barrio,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    # Dirección exacta del cliente.
    # Ejemplo: Calle 10 #15-20 apto 302
    direccion = models.CharField(max_length=50)

    # Fecha automática de creación del checkout.
    fecha = models.DateTimeField(auto_now_add=True)

    # Representación legible del checkout.
    def __str__(self):
        return f"Checkout #{self.id} - {self.cliente}"



# =========================
# MODELO PAGO
# =========================

# Este modelo almacena la información del pago realizado.
class Pago(models.Model):

    # Relación uno a uno:
    # Cada checkout tiene un único pago asociado.
    checkout = models.OneToOneField(
        Checkout,
        on_delete=models.CASCADE
    )

    # Lista de métodos de pago disponibles.
    # choices crea opciones seleccionables en formularios/admin.
    METODOS_PAGO = [
        ("Tarjeta", "Tarjeta"),
        ("PSE", "PSE"),
        ("Contra entrega", "Contra entrega"),
    ]

    # Campo para guardar el método elegido.
    # Por defecto será contra entrega.
    metodo_pago = models.CharField(
        max_length=30,
        choices=METODOS_PAGO,
        default="Contra entrega"
    )

    # Estados posibles del pago.
    ESTADOS = [
        ("Pendiente", "Pendiente"),
        ("Aprobado", "Aprobado"),
        ("Rechazado", "Rechazado"),
    ]

    # Estado actual del pago.
    # Por defecto inicia en pendiente.
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="Pendiente"
    )

    # Referencia única del pago.
    # Sirve como identificador o comprobante.
    referencia = models.CharField(max_length=20, unique=True)

    # Fecha en que se registró el pago.
    fecha_pago = models.DateTimeField(auto_now_add=True)

    # Representación legible del pago.
    def __str__(self):
        return f"Pago {self.referencia}"