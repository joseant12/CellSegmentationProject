from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre: models.CharField(max_length=50,default=False)
    email: models.CharField(max_length=25,default=False)
    password: models.CharField(max_length=20)

class Coleccion(models.Model):
    titulo = models.CharField(max_length=16,default="DefaultTitle")
    description = models.TextField(max_length=255,default="DefaultDescription")

#falta usuario

class Image(models.Model):
    """
    Modelo de la imagen. 
    Titulo de tipo  CharField con un máximo de 16 caracteres.
    Descripción de tipo  TextField con un máximo de 255 caracteres.
    Imagen de tipo ImageField.
    """
    fk_Coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
    image_File = models.FileField(default='defaul2.png',upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True,blank=True)


#condo = models.ForeignKey(Condo, on_delete=models.CASCADE, related_name='images')