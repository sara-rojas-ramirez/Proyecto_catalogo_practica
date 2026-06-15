from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm



# La vista de login 
# Esta función maneja dos procesos (petición GET) y (petición POST)
def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username = username,
                password = password
            )

            if user is not None:
                login(request, user)

                if user.is_superuser:
                    return redirect('admin_dashboard')
                else:
                    return redirect('catalogo')
    
    return render(request, 'accounts/login.html', {
        'form': form
    })




# Funcionalidad de logout
# Recibe la petición de cerrar sesión, ejecuta logout(request), borrando las cookies y la sesión activa del usuario y redirige a la pantalla de login.
def logout_view(request):
    logout(request)
    return redirect('login')