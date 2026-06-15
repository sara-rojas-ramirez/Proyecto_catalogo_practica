
from django import forms

# Creación del formulario HTML de login

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Ingrese usuario",
        max_length=50
    )

    password = forms.CharField(
        label="Ingrese contraseña",
        widget=forms.PasswordInput
    )

