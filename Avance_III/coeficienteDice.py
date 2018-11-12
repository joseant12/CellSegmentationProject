#Librerias
import numpy as np
import cv2


#Funciones
def coeficienteDice(archivo1, archivo2):
    """
    Calcula el coeficiente de Dice
    @param archivo1 nombre o ruta de la imagen a comparar
    @param archivo2 nombre o ruta de la imagen a comparar
    @return retorna el resultado del calculo en un numero de tipo float
    """
    try:
        imagen1 = cv2.imread(archivo1)
        imagen2 = cv2.imread(archivo2)
        imagen1a = np.asarray(imagen1).astype(np.bool)
        imagen2a = np.asarray(imagen2).astype(np.bool)
        interseccion = np.logical_and(imagen1a, imagen2a)
        coeficiente = (2. * interseccion.sum()) / (imagen1a.sum() + imagen2a.sum())
        return coeficiente 
    except:
        print("Error")
        return False


#print(coeficienteDice("1.png", "1_pred.png"))
