
# Importanciones esenciales 
from django import forms 
from django.contrib.auth.models import User
from .models import Cliente


# Formulario forms
class RegistroForm(forms.Form):
    # Campo de username
    username = forms.CharField(
        label = "Usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese usuario'
        })
    )

    # Campo de email
    email = forms.EmailField(
        label = "Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese correo'
        })
    )

    # Campo de telefono
    telefono = forms.CharField(
        label = "Telefono",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese teléfono'
        })
    )

    # Campo de contraseña
    password = forms.CharField(
        label = "Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese contraseña'
        })
    )

    # Campo de confirmación de contraseña
    confirmPassword = forms.CharField(
        label = "Confirmación contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })
    )


    # Validaciones basicas del registro
    # Validar nombre de usuario
    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username = username).exists():
            raise forms.ValidationError("Este usuario ya existe.")
        return username

    # Validar telefono
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']

        if Cliente.objects.filter(telefono = telefono).exists():
            raise forms.ValidationError('Este teléfono ya esta registrado.')
        
    # Validar contraseñas
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirmPassword')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coindicen.')

        return cleaned_data


