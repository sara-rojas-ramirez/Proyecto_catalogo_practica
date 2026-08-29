from django.db import models
from django.contrib.auth.models import User

# Modelo cliente
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    telefono = models.CharField(max_length=20, unique=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username



# Modelo Roles
class Perfil(models.Model):

    ROLES = [
        ('Admin', 'Administrador'),
        ('cliente', 'Cliente')
    ]

    rol = models.CharField(max_length=20, choices=ROLES)