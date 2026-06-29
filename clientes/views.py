from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Cliente
from .forms import RegistroForm

# Vistas y logica de registro
def registroView(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
    
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )

            Cliente.objects.create(
                user=user,
                telefono=form.cleaned_data["telefono"]
            )

            return redirect("catalogo")
    else:
        form = RegistroForm()

    return render(request, "accounts/registro.html", {
        "form": form
    })
