import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.models import model_from_json
from keras.models import load_model

model =None

def main():


    model= cargar_modelo('best_female_model.h5')
    model=compiler_modelo(model)


def cargar_modelo(nombre_modelo):


    modelo_read=Sequential()
    modelo_read.load_weights(nombre_modelo,by_name=True)

    return modelo_read

def compiler_modelo(modelo):

    modelo.compile(loss='mean_squared_error',optimizer='adam',metrics=['binary_accuaracy'])
    print("Modelo Compilado")
    return modelo

if __name__=="__main__":
    main()
