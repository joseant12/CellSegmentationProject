'''
Created on 23 ago. 2018

@author: ganso
'''


import unittest
from modelo import*
#Modulo de pruebas unitarias

class TestKeras(unittest.TestCase):
    
    
 
         
    def test_carga_modelo(self):
        
        modelo_test=cargar_modelo("best_female_model.h5")
        self.assertNotEqual(modelo_test,None , "Modelo No cargado")
        
        #None la funcion no regreso el objecto 
    
   
    
    def test_compilacion_modelo(self): 
        
        modelo_test=cargar_modelo("best_female_model.h5")
        
        modelo_compiler=compiler_modelo(modelo_test)
        print(modelo_compiler)
        self.assertNotEqual(modelo_compiler, None, "Modelo No Compilado")
        
        #None la funcion no regreso el objecto 
        
         
        
if __name__=="__main__":
    unittest.main()
        
        
        
        
        