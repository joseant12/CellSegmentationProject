import sys
sys.path.append("..")
from .Adaptador import Adaptador
from django.test import TestCase

# Create your tests here.
class TestAnalizador(TestCase):
    def test_integracion_analizador(self):
        Adap = Adaptador()
        Adap.analizar('../media/images/0/*.png')
