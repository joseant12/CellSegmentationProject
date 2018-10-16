'''
Created on 15 oct. 2018

@author: ganso
'''
import unittest
from segmentacion import load_test_data
from segmentacion import  dice_coef



class Test(unittest.TestCase):


    def test_load_test_data(self):
    
        raw_imagen=load_test_data('114.png')
        print(raw_imagen)
        self.assertNotEqual(raw_imagen,[[],{}],'Error Prueba 1')
    
    
    def test_dice_coef(self):
        
        test=dice_coef(0,'h')
        self.assertNotEqual(test,None,'Error Prueba 2')     

if __name__=="__main__":
    unittest.main()