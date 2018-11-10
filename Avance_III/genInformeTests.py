#Librerias
import unittest
from genInforme import *


#Pruebas
"""
testInforme1: prueba si la generacion del archivo .csv se hizo correctamente
testInforme2: prueba si la creacion de la lista con los resultados tuvo un error o no
"""
class Test(unittest.TestCase):
    def testInforme1(self):
        datos = {'test1':[12345,67890], 'test2':[9876,54321]}
        df = pd.DataFrame(datos)
        resultado = generarArchivoCSV('test.csv', df)
        self.assertTrue(resultado)

    def testInforme2(self):
        resultado = getListaCelulas('22.png')
        self.assertIsNotNone(resultado)

if __name__=="__main__":
    unittest.main()
