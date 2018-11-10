import sys
sys.path.append("..")
from django.test import TestCase
from .views import *


class TestAdaptador(TestCase):
    def test_has_no_preds(self):
        """Función que comprueba el comportamiento del método has_preds cuando no se tienen predicciones
        @return 2 assert que compara los arreglos img_paths y preds_paths con valores vacíos. 
        """
        img_paths, preds_paths, counts = has_preds(1)
        self.assertEqual(img_paths,["/media/images/1/preds"])
        self.assertEqual(preds_paths,[])

    def test_has_preds(self):
        """Función que comprueba el comportamiento del método has_preds cuando se tienen predicciones
        @return 2 assert que compara los arreglos img_paths y preds_paths con valores correspondientes a las imágenes de la carpeta 0. 
        """
        img_paths, preds_paths, counts = has_preds(0)
        self.assertEqual(img_paths,['/media/images/0/1.png','/media/images/0/2.png', '/media/images/0/preds'])
        self.assertEqual(preds_paths,['/media/images/0/preds/1.png', '/media/images/0/preds/2.png'])