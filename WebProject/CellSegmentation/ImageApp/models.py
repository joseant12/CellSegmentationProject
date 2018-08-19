from django.db import models

# Create your models here.
class Image(models.Model):
    """
    Modelo de la imagen. 
    Titulo de tipo  CharField con un máximo de 16 caracteres.
    Descripción de tipo  TextField con un máximo de 255 caracteres.
    Imagen de tipo ImageField.
    """
    title = models.CharField(max_length=16,default="DefaultTitle")
    description = models.TextField(max_length=255)
    imageField = models.ImageField(default='defaul.png',blank=True)