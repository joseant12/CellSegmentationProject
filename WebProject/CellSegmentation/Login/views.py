from django.http import HttpResponse
from django.shortcuts import render
import sys
sys.path.append('..')
from ImageApp.models import Usuario


def login_view(request):
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