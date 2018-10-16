from django.http import HttpResponse
from django.shortcuts import render
import sys
sys.path.append('..')
from ImageApp.models import Usuario


def login_view(request):
    """
    Función perteneciente a la vista que recibe los datos del formulario y se encarga de instanciar el login
    @param request: recibe los datos del usuario (email,password) capturados luego del POST del formulario
    @return render del formulario con el form vacío.
    """
    if request.method == 'POST':
        email = request.POST.get("usuario","")
        contrasena = request.POST.get("password","")
        try:
            usuario_object = Usuario.objects.get(email=email,password=contrasena)
            print(usuario_object.id)
            request.session['usuario_id'] = usuario_object.id
        except Usuario.DoesNotExist:
            print("No se pudo obtener")
        print(request.POST.get("usuario",""))
    return render(request, 'login_form.html')