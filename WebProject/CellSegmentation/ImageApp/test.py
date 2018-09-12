import sys
sys.path.append("..")
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
from .forms import ColeccionForm
from . import forms

class TestImagenes(TestCase):
        def test_form(self):
                #upload_file = open('path/to/file', 'rb')
                form_data = {'titulo':'titulo','descripcion':'descripcion'}
                form = ColeccionForm(data=form_data)
                self.assertTrue(form.is_valid())
