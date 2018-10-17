from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import sys
sys.path.append('..')
from ImageApp.models import Usuario
from ImageApp.models import Coleccion


def login_view(request):
    """
    Función perteneciente a la vista que recibe los datos del formulario y se encarga de instanciar el login
    @param request: recibe los datos del usuario (email,password) capturados luego del POST del formulario
    @return render del formulario con el form vacío.
    """
    alert = False
    if request.method == 'POST':
        email = request.POST.get("usuario","")
        contrasena = request.POST.get("password","")
        try:
            usuario_object = Usuario.objects.get(email=email,password=contrasena)
            request.session['usuario_id'] = usuario_object.id
            return redirect('analizador:list')
            #return render(request, 'Colection_List.html', {'colecciones':colecciones}) 
        except Usuario.DoesNotExist:
            alert = True
            print("No se pudo obtener")
        print(request.POST.get("usuario",""))
    return render(request, 'login_form.html', {'alert':alert})