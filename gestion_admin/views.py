from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

# Vista de gestión administrador, solo los usuarios staff pueden entrar
@staff_member_required
def dashboard(request):
    return render(request, 'gestion/gestion.html')