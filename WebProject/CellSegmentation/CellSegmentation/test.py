import sys
sys.path.append("..")
import cv2
from .Adaptador import Adaptador
from Analizador.views import download_files
from ImageApp.models import Coleccion
from ImageApp.models import Usuario
from .contador import generar_informe, getContornos

from django.test import TestCase,  RequestFactory

# Create your tests here.
class TestAnalizador(TestCase):
    def test_integracion_analizador(self):
        """ Prueba de integración que prueba la unión del módulo analizador y conteo de células.
        @return assert con un valor booleano del resultado del análisis de la colección 51
        """
        Adap = Adaptador()
        analizador = Adap.analizar('../media/images/51/*.png',51)
        self.assertTrue(analizador)

    def test_analizador_coleccion(self):
        """ Prueba de integración que prueba el comportamiento del módulo de colección con el analizador
        @return assert que compara si el tiempo de la colección analizada ha cambiado
        """
        Adap = Adaptador()
        usuario1 = Usuario()
        usuario1.save()
        coleccion1 = Coleccion()
        coleccion1.id = 51
        coleccion1.fk_Usuario = usuario1
        coleccion1.titulo = "."
        coleccion1.descripcion = "."
        coleccion1.tiempo = 'Sin analizar'
        coleccion1.save()
        analizador = Adap.analizar('../media/images/51/*.png', coleccion1.id)
        coleccion2 = Coleccion.objects.get(id = 51)
        self.assertTrue(coleccion1.tiempo != coleccion2.tiempo)

    def test_download_files(self):
        self.factory = RequestFactory()
        coleccion1 = Coleccion()
        coleccion1.id = 51
        response = self.factory.get('predictions/download/51/')
        respuesta = download_files(response,coleccion1.id)
        self.assertIsNotNone(respuesta)
    
    def test_contador_celulas(self):
        image =cv2.imread("11.png")
        cnts=getContornos(image)
        dataframe = generar_informe(cnts)
        self.assertIsNotNone(dataframe)

