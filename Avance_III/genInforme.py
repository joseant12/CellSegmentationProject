#Librerias
import cv2
import pandas as pd
from contador import getContornos

#Funciones
def getListaCelulas(archivo):
    """
    Genera una lista de tipo DataFrame con los resultados obtenidos del analisis de la imagen
    @param archivo el nombre o la ruta de la imagen a analizar
    @return retorna un dato tipo DataFrame
    """
    try:
        imagen = cv2.imread(archivo)
        contornos = getContornos(imagen)
        listaCelulas = []
        listaCoordenadasX = []
        listaCoordenadasY = [] 
        listaAreas = []
    
        for(n, c) in enumerate(contornos):
            ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
            area = cv2.contourArea(c)
            listaCelulas.append(n)
            listaCoordenadasX.append(centerX)
            listaCoordenadasY.append(centerY)
            listaAreas.append(area)

        datos = {'Celula':listaCelulas, 'CentroideCoordenadaX':listaCoordenadasX, 'CentroideCoordenadaY':listaCoordenadasY, 'Area':listaAreas}
        df = pd.DataFrame(datos)
        return df
    except:
        print("Error")
        return None

def generarArchivoCSV(nombreArchivo, datos):
    """
    Genera un nuevo archivo tipo CSV.
    @param nombreArchivo nombre del archivo CSV en donde se desea guardar, por ejemplo: "new.csv".
    @param datos tipo de dato DataFrame de la libreria Pandas.
    @return retorna un valor de True si no ocurrio ningun error al generar el archivo, y un False en caso contrario.
    """
    try:
        datos.to_csv(nombreArchivo, index=False)
        return True
    except:
        return False

#generarArchivoCSV('resultados.csv', getListaCelulas('22.png'))
