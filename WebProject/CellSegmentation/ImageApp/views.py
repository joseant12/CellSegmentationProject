from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .models import Image
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
            for file in request.FILES.getlist('images'):
                print("Imagen 111")
                instance = Image(
                    title = request.POST.get("title",""),
                    description = request.POST.get("description",""),
                    image_File=file
                )
            instance.save()
    else:
        form = forms.ImageForm()
    return render(request, 'Image_form.html', { 'form': form })