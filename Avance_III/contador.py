
from __future__ import print_function
import numpy as np
import argparse
import cv2
import random


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
                            # first argument we make a copy second argument is the outermost Contours
                            # third argument is the compress horizonta
    return cnts

def pintarCelulas(ruta):

    image =cv2.imread(ruta)
    cnts=getContornos(image)
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
    #cv2.imshow('s',image)
    #cv2.waitKey(0)
    cv2.imwrite("9.png",image)
    return True


pintarCelulas('22.png')
