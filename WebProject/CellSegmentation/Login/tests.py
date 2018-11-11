from urllib.parse import urlencode
import sys
sys.path.append("..")
from django.test import TestCase, RequestFactory
from .views import *

# Create your tests here.
class TestLogin(TestCase):
    def test_autentificacion(self):
        """Función que se encarga de evaluar el sistema de login con un usuario y contraseña válidos.
        @return assert que evalua si el usuario pudo loggearse adecuadamente
        """
        self.factory = RequestFactory()
        data = urlencode({"usuario": "user2@gmail.com", "password": "123"})
        response = self.factory.get('/authentication/login')
        response.post = data
        retorno = login_view(response)
        self.assertTrue(retorno)

