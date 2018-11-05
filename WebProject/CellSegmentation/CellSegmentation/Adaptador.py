from . import unet_CellSegmentation as keras
class Adaptador():
    def __init__(self):
        pass

    def analizar(self,path,coleccion):
        """Función encargada de invocar el segmentador de células
        @param path: Ubicación de la carpeta contenedora de las imágenes a analizar
        """
        keras.analyze(path,coleccion)
