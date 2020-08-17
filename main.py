# Taller 1: Proc, de imagnes y vision

import os
import numpy as np
import cv2
from colorImage import * # Clase creada


if __name__ == '__main__': #Main
    print('Ingrese la ruta de la imagen')
    ruta = input()
    a = colorImage(ruta) #Se carga y se visualiza la imagen original

    a.displayProperties() #  Se imprime el ancho y alto de la imagen

    img_gris = a.makeGray() # Retorna la imagen en grises
    cv2.imshow('Gris', img_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img_colorizada= a.colorizeRGB('red') #Retorna una version rojiza de la imagen
    cv2.imshow('Colorizada-Img', img_colorizada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img_hsv = a.makeHue() #Retorna una version con tonos/colores resaltados
    cv2.imshow('HSV', img_hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

