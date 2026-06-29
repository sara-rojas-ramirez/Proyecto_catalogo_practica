
from django import forms

# Creación del formulario HTML de login

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuario', # El label va aquí
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresar usuario'
        })
    )

    password = forms.CharField(
        label='Contraseña', # El label va aquí
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresar contraseña'
        })
    )



