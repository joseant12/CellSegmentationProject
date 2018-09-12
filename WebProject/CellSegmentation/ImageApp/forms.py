from django import forms
from .models import Image
from .models import Coleccion


class ImageForm(forms.ModelForm):
    """
    Formulario para la creación de una instancia de imagen
    """
    class Meta:
        model = Image
        fields = [
        ]
class ColeccionForm(forms.ModelForm):
    """
    Formulario para la creación de una instancia de coleccion
    """
    class Meta:
        model = Coleccion
        fields = [
            'titulo',
            'descripcion'
        ]