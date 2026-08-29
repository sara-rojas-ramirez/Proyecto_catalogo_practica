
# Importaciones:
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Cliente
from .forms import RegistroForm

# RegistroView
def registroView(request):
    # Si el metodo es POST, significa que el usuario envio la petición del formulario, por lo tanto: 
    if request.method == 'POST':
        # Se crea una instancia de formulario de RegistroForm y se llena con los usuarios enviados por el usuario
        form = RegistroForm(request.POST)

        # Valida el formulario y comprueba que si cumpla con las reglas definidas en Cliente/forms.py 
        if form.is_valid():
            # Crea el usuario en la bd
            # Usa el modelo User de Django para registrar un nuevo usuario con nombre, correo y contraseña.
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )

            # Crea el objeto Cliente asociado al usuario
            Cliente.objects.create(
                user=user,
                telefono=form.cleaned_data["telefono"]
            )

            # Redirije al catalogo
            return redirect("catalogo")
    else:
        # Si el metodo no es POST, muestra el form vacio
        form = RegistroForm()

    # Renderiza la pantalla
    # Devuelve la página registro.html con el formulario (ya sea vacío o con errores si la validación falló).
    return render(request, "accounts/registro.html", {
        "form": form
    })
