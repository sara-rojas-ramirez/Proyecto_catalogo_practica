
# Importa el módulo de formularios de django
from django import forms

# Se define una clase para el formulario de inicio de sesión
class LoginForm(forms.Form):
    # Crea un campo de texto para el usuario
    username = forms.CharField(
        label='Usuario',

        # Define el tipo de input HTML (texto)
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresar usuario'
        })
    )

    # Crea un campo para la contraseña
    password = forms.CharField(
        label='Contraseña',

        # Define el tipo de input HTML (en este caso password) y attrs agrega los atributos HTML como form-control (para aplicar estilos de Bootstrap) y el placeholder
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresar contraseña'
        })
    )



