from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    """
    Formulario para la creación de una instancia de imagen
    """
    class Meta:
        model = Image
        fields = [
            'title',
            'description',
            'imageField'
        ]