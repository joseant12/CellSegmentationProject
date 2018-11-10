from . import unet_CellSegmentation as keras
import sys
sys.path.append('..')
from ImageApp.models import Coleccion
import time

class Adaptador():
    def __init__(self):
        pass

    def analizar(self,path,coleccion):
        """Función encargada de invocar el segmentador de células
        @param path: Ubicación de la carpeta contenedora de las imágenes a analizar
        """
        t0 = time.time()
        keras.analyze(path,coleccion)
        t1 = time.time()
        total = t1-t0
        total = str(round(total,4)) + " seg"
        Coleccion.objects.filter(id = coleccion).update(tiempo = total)
        print("tiempo total: "+str(total))
