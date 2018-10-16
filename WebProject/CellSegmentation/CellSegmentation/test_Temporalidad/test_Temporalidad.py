import time
from . import unet_CellSegmentation as keras

def invocar_funcion(duration=0.000001):
    keras.analyze('../media/images/10/*.png')
    time.sleep(duration)
    return True

def test_temporalidad(benchmark):
    """Función que evalua el tiempo que tarda el módulo segmentador procesando 50 imágenes
    @return: un informe del benchmark con la media, min, max de tiempo.
    """
    result = benchmark(invocar_funcion)

    assert result is True