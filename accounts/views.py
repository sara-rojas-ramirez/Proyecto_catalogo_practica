
# Importaciones del form, autenticación, redirección, render, Json
from django.shortcuts import render, redirect
from django.http import JsonResponse
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

                if user.is_staff:
                    return redirect('gestion_dashboard')
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




# Vista para la implementación de AJAX para Login
def login_ajax(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        contraseña = request.POST.get('password')

        user = authenticate(request, username = usuario, password=contraseña)

        if user is not None:
            login(request, user)
            return JsonResponse({'valido': True, 'redirect_url': '/'})
        else:
            return JsonResponse({'valido': False, 'mensaje': 'Usuario o contraseña incorrectos.'})
    
    return JsonResponse({'valido': False, 'mensaje': 'Método no permitido.'}, status=405)





