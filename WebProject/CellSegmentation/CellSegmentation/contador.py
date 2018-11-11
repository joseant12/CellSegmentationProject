from __future__ import print_function
import numpy as np
import pandas as pd
import argparse
import cv2
import random

def generar_informe(cnts):
    listaCelulas = []
    listaCoordenadasX = []
    listaCoordenadasY = [] 
    listaAreas = []
    for(n, c) in enumerate(cnts):
        ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
        area = cv2.contourArea(c)
        listaCelulas.append(n)
        listaCoordenadasX.append(centerX)
        listaCoordenadasY.append(centerY)
        listaAreas.append(area)
    datos = {'Celula':listaCelulas, 'CentroideCoordenadaX':listaCoordenadasX, 'CentroideCoordenadaY':listaCoordenadasY, 'Area':listaAreas}
    df = pd.DataFrame(datos)
    return df

def getCantidadCelulas(ruta):
    image =cv2.imread(ruta)
    contornos=getContornos(image)
    return len(contornos)-1

def getContornos(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #escala de grises
    blurred = cv2.GaussianBlur(gray,(9,9),0)  #suavisado de imagen
    edge = cv2.Canny(blurred,30,150) # detecta bordes
    (_,cnts,_) = cv2.findContours(edge.copy(),cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    return cnts

def pintarCelulas(ruta, coleccion, nombre_Archivo):

    image =cv2.imread(ruta)
    cnts=getContornos(image)
    informe = generar_informe(cnts)
    image[np.where(image!=[0])] = [255]
    for (i, c) in enumerate(cnts):

        (x, y, w, h) = cv2.boundingRect(c)

        coin = image[y:y + h, x:x + w]
        coin[np.where((coin == [255,255,255]).all(axis = 2))] = [random.randrange(255),random.randrange(255),random.randrange(255)]
        image[y:y + h, x:x + w]=coin

        ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
        font = cv2.FONT_HERSHEY_SIMPLEX

        ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
        cv2.putText(image,str(i),(int(centerX), int(centerY)), font, 0.3,(255,255,255))
        
    new_path = "../media/images/" + str(coleccion) + "/preds/count/"
    informe_path = "../media/images/" + str(coleccion) + "/preds/report/"
    string_path = new_path + str(nombre_Archivo) + ".png"
    nombre_informe = informe_path + str(nombre_Archivo) + ".csv"
    cv2.imwrite(string_path,image)
    informe.to_csv(nombre_informe, index=False)
    return True