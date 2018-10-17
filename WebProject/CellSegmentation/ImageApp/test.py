import sys
sys.path.append("..")
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
from .forms import ColeccionForm
from . import forms

class TestImagenes(TestCase):
        def test_format(self):
                """Función que evalua si el formato de una imagen se conserva
                @return: resultado de prueba comparando si la imagen es formato png
                """
                coleccion_objeto = Coleccion()
                image_objeto = Image()
                image_objeto.image_File = SimpleUploadedFile(name='black.png', content=open('../../black.png', 'rb').read(), content_type='image/png')
                image_objeto.fk_Coleccion = coleccion_objeto
                self.assertEqual(image_objeto.load_image_function().format,'PNG')

        def test_add_photo(self):
                """Función que evalua si la base de datos guarda satisfactoriamente la imagen
                @return: resultado de prueba comparando si la colección de objetos tiene un tamaño de 1
                """
                coleccion_objeto = Coleccion()
                coleccion_objeto.save()
                image_objeto = Image()
                image_objeto.image_File = SimpleUploadedFile(name='black.png', content=open('../../black.png', 'rb').read(), content_type='image/png')
                image_objeto.fk_Coleccion = coleccion_objeto
                image_objeto.save()
                self.assertEqual(Image.objects.count(), 1)

        def test_size(self):
                """Función que evalua si el tamaño de la imagen guardada corresponde a la original
                @return: resultado de prueba comparando si la imagen guardada tiene las mismas dimensiones.
                """
                coleccion_objeto = Coleccion()
                image_objeto = Image()
                image_objeto.image_File = SimpleUploadedFile(name='black.png', content=open('../../black.png', 'rb').read(), content_type='image/png')
                image_objeto.fk_Coleccion = coleccion_objeto
                self.assertEqual(image_objeto.load_image_function().size,(275,183))

        def test_form(self):
                """Función que evalua si el formulario es valido
                @return: retorna la condición en la cual se encuentra el formulario de colección.
                """
                form_data = {'titulo':'titulo','descripcion':'descripcion'}
                form = ColeccionForm(data=form_data)
                self.assertTrue(form.is_valid())

        def test_add_user(self):
                usuario = Usuario()
                usuario.nombre = "Usuario prueba"
                usuario.email = "usuario@user.com"
                usuario.password = "pass123"
                usuario.save()
                self.assertEqual(Usuario.objects.count(), 1)

