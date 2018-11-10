from django.db import models
from PIL import Image as Image_Import
import uuid

def images_directory_path(instance, filename):
    return '/'.join(['images', str(instance.fk_Coleccion.id), str(uuid.uuid4().hex + ".png")])

class Usuario(models.Model):
    nombre= models.CharField(max_length=50,blank=False)
    email= models.CharField(max_length=25,default=False,blank=False)
    password= models.CharField(max_length=20,default=False,blank=False)

class Coleccion(models.Model):
    fk_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default = False)
    titulo = models.CharField(max_length=16,default="DefaultTitle")
    descripcion = models.TextField(max_length=255,default="DefaultDescription")
    tiempo = models.TextField(max_length=32,default="Sin analisis previo")

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

    def load_image_function(self):
        pngfile = Image_Import.open(self.image_File)
        return pngfile


#condo = models.ForeignKey(Condo, on_delete=models.CASCADE, related_name='images')