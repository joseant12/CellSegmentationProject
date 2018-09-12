import sys
sys.path.append("..")
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
from .forms import ColeccionForm
from . import forms

class TestImagenes(TestCase):
        def test_add_photo(self):
                coleccion_objeto = Coleccion()
                coleccion_objeto.save()
                image_objeto = Image()
                image_objeto.image_File = SimpleUploadedFile(name='black.png', content=open('../../black.png', 'rb').read(), content_type='image/png')
                image_objeto.fk_Coleccion = coleccion_objeto
                image_objeto.save()
                self.assertEqual(Image.objects.count(), 1)

        def test_size(self):
                coleccion_objeto = Coleccion()
                image_objeto = Image()
                image_objeto.image_File = SimpleUploadedFile(name='black.png', content=open('../../black.png', 'rb').read(), content_type='image/png')
                image_objeto.fk_Coleccion = coleccion_objeto
                self.assertEqual(image_objeto.load_image_function(),(275,183))

        def test_form(self):
                form_data = {'titulo':'titulo','descripcion':'descripcion'}
                form = ColeccionForm(data=form_data)
                self.assertTrue(form.is_valid())
