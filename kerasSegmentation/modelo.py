import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.models import model_from_json
from keras.models import load_model

model =None #variable donde se va a cargar el modelo .h5

def main():


    model= cargar_modelo('best_female_model.h5')
    model=compiler_modelo(model)


def cargar_modelo(nombre_modelo):
    """
    Carga un modelo previamente generado por keras, con formato .h5.
    @param nombre_modelo nombre del modelo .h5 que se desea cargar, sea tambien la ruta donde se ubica el modelo.
    @return regresa un objecto con el modelo de los pesos cargado.
    """
    modelo_read=Sequential()
    modelo_read.load_weights(nombre_modelo,by_name=True)

    return modelo_read


def compiler_modelo(modelo):
    """
    Compila un modelo previamente cargado para luego ser ejecutado.
    @param modelo objecto con el modelo previamente cargado.
    @return modelo objecto con el modelo compilado.
    """
    modelo.compile(loss='mean_squared_error',optimizer='adam',metrics=['binary_accuaracy'])
    print("Modelo Compilado")
    return modelo

    #si el objecto no es pasado por referencia y en vez solo se instacia a la funcion sea
    #model =compiler_modelo()
    #puede que el modelo no se compile correctamente o no lo haga del todo.

if __name__=="__main__":
    main()
