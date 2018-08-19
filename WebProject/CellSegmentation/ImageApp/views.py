from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from . import forms



# Create your views here.
def home_view(request, *args, **kwargs):
    
    my_context = {
        "my_text": "About the author"
    }
    return render(request,"home.html",my_context) 

def Image_form_view(request):
    form = ImageForm(request.POST or None)
    if form.is_valid():
         form.save()
    context = {
        'form' : form
    }
    return render(request, "Image_form.html", context)

def image_create(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = forms.ImageForm()
    return render(request, 'Image_form.html', { 'form': form })