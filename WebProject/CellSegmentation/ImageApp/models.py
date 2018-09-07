from django.db import models
import uuid

def images_directory_path(instance, filename):
    return '/'.join(['images', str(instance.fk_Coleccion.id), str(uuid.uuid4().hex + ".png")])


class Usuario(models.Model):
    nombre: models.CharField(max_length=50,default=False)
    email: models.CharField(max_length=25,default=False)
    password: models.CharField(max_length=20)

class Coleccion(models.Model):
    titulo = models.CharField(max_length=16,default="DefaultTitle")
    descripcion = models.TextField(max_length=255,default="DefaultDescription")

#falta usuario

class Image(models.Model):
    """
    Modelo de la imagen. 
    Titulo de tipo  CharField con un máximo de 16 caracteres.
    Descripción de tipo  TextField con un máximo de 255 caracteres.
    Imagen de tipo ImageField.
    """
    fk_Coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, default = False)
    image_File = models.FileField(default='defaul2.png',upload_to=images_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True,blank=True)


#condo = models.ForeignKey(Condo, on_delete=models.CASCADE, related_name='images')