from . import unet_CellSegmentation as keras

class Adaptador():
    def __init__(self):
        pass

    def analizar(self,path):
        #h
        keras.analyze(path)
