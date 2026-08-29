
# Importaciones:
# render: muestra una plantilla HTML
# redirect: redirige a otra página
# JsonResponse: devuelve datos en formato JSON (bastante útil para AJAX)
# authenticate: verifica usuario y contraseña
# login: inicia sesión
# logout: cierra sesión
# Por último, se importa el formulario de forms.py dentro de accounts/

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


# Login_view: maneja el login tradicional con recarga de página
def login_view(request):
    # Crea el formulario vaciO (GET)
    form = LoginForm()

    # Si el usuario envio el formulario, entonces:
    if request.method == "POST":
        # Llena el formulario con los datos enviados
        form = LoginForm(request.POST)

        # Valida que los datos sean correctos con is_valid (que los campos no esten vacios, etc)
        if form.is_valid():
            # Limpieza de datos (sanitización), eso significa que convierte los datos nativos de Python y los sanitiza de manera que esten limpios de posibles ataques maliciosos
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Comprueba si las credenciales existen en la BD de la siguiente forma: Busca al usuario, toma la contraseña y la encripta paraa despues compararla con la contrasela hash guardada. Si es correcto devuelve user y si no, devuelve None
            user = authenticate(
                request,
                username = username,
                password = password
            )

            # Si el usuario es diferente de None, entonces:
            if user is not None:
                # Inicia sesión, recibiendo request como la petición actual y user como el usuario autenticado
                login(request, user)

                # Si es administrador, redirige a dashboard
                if user.is_staff:
                    return redirect('gestion_dashboard')
                else:
                    # Si es un cliente, redirige al catalogo
                    return redirect('catalogo')
    
    # Renderizado final 
    return render(request, 'accounts/login.html', {
        'form': form
    })
    # messages para mas adelante



# Logout_view: Borra la sesión activa
def logout_view(request):
    # Recibe la petición de cerrar sesión, ejecuta logout(request), borrando las cookies y la sesión activa del usuario y redirige a la pantalla de login.
    logout(request)
    return redirect('login')




# login_ajax: realiza lo mismo que login_view, pero sin recargar la página y usando AJAX
# def login_ajax(request):
    
#     if request.method == 'POST':
#         usuario = request.POST.get('username')
#         contraseña = request.POST.get('password')

#         user = authenticate(request, username = usuario, password=contraseña)

#         if user is not None:
#             login(request, user)
#             return JsonResponse({'valido': True, 'redirect_url': '/'})
#         else:
#             return JsonResponse({'valido': False, 'mensaje': 'Usuario o contraseña incorrectos.'})
    
#     return JsonResponse({'valido': False, 'mensaje': 'Método no permitido.'}, status=405)




