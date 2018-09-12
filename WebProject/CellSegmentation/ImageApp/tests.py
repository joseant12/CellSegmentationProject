#./manage.py test ImageApp.test.TestImagenes
import sys
sys.path.append("..")
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
from .forms import ColeccionForm
from . import forms

class TestImagenes(TestCase):
        def test_size(self):
                form_data = {'titulo':'titulo','descripcion':'descripcion'}
                coleccion_objeto = ColeccionForm(data=form_data)
                image_file = open('../black.png', 'rb')
                form_data = {'fk_Coleccion':coleccion_objeto,'image_File':image_file}
                objeto = Image(form_data)
                self.assertEqual(objeto.load_image_function(),(720,649))

        def test_form(self):
                #upload_file = open('path/to/file', 'rb')
                form_data = {'titulo':'titulo','descripcion':'descripcion'}
                form = ColeccionForm(data=form_data)
                self.assertTrue(form.is_valid())

