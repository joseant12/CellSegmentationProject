#Librerias
import pandas as pd

#Funciones para el manejo de archivos .csv

def leerArchivoCSV(nombreArchivo):
    """
    Abre y lee un archivo de tipo CSV.
    @param nombreArchivo nombre del archivo CSV que se desea leer, por ejemplo: "ejemplo.csv".
    @return retorna los datos del archivo CSV como un DataFrame.
    """
    try:
        df = pd.read_csv(nombreArchivo)
        return df
    except:
        print("Archivo no existe")

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
