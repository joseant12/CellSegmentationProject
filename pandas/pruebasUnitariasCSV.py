'''
Created on 22 ago. 2018

@author: Yin Cheng
'''
import unittest
from manejoArchivosCSV import *

#Modulo de pruebas unitarias
"""
test1: prueba si se pudo abrir, leer los datos y almacenarlo a la variable
test2: prueba si al no encontrar el archivo retorna False
test3: prueba si retorna False al querer crear un archivo con datos incorrectos
test4: prueba si se pudo generar un nuevo archivo CSV con datos y retorna True
"""
class TestCSV(unittest.TestCase):
    def testLeerCSV1(self):
        resultado=leerArchivoCSV("train.csv")
        self.assertIsNotNone(resultado)

    def testLeerCSV2(self):
        resultado=leerArchivoCSV("archivoX.csv")
        self.assertFalse(resultado)

    def testGenerarCSV1(self):
        resultado=generarArchivoCSV("new.csv", 'datos')
        self.assertFalse(resultado)

    def testGenerarCSV2(self):
        resultado=generarArchivoCSV("new.csv", pd.DataFrame({'nombre':['nombre1','nombre2','nombre3'],'apellido':['apellido1','apellido2','apellido3'],'edad':[12,15,21]}))
        self.assertTrue(resultado)

if __name__=="__main__":
    unittest.main()
