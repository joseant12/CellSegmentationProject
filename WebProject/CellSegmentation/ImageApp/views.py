from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from .models import Coleccion
from . import forms



# Create your views here.

def image_create(request):
    """
    Función perteneciente a la vista que recibe los datos del formulario y se encarga de instanciar la imagen
    @param request: recibe los datos (titulo,descripción,imagen) capturados luego del POST del formulario
    @return render del formulario con el form vacío.
    """
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            coleccion_padre = Coleccion(
                            titulo = request.POST.get("title",""),
                            descripcion = request.POST.get("description",""),
            )
            coleccion_padre.save()
            for file in request.FILES.getlist('images'):
                instancia = Image(
                            fk_Coleccion = coleccion_padre,
                            image_File = file
                )
                instancia.save()
    else:
        form = forms.ImageForm()
    return render(request, 'Image_form.html', { 'form': form })