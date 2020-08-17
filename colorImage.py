import os
import numpy as np
import cv2
class colorImage:
    def __init__(self, ruta):
        # Cargamos la imagen de la ruta especificada
        self.imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)

        # mostramos la imagen
        cv2.imshow('Lena', self.imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def displayProperties(self):
        img = self.imagen
        tam = img.shape
        print('Propiedades: ',tam)

    def makeGray(self):
        img_gris = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        return img_gris

    def colorizeRGB(self, canal):
        img_gris = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY) #Se pasa la imagen a escala de grises (queda solo en dos canales)
        img_convertida = cv2.cvtColor(img_gris, cv2.COLOR_GRAY2RGB) #La imagen se pasa a tres canales pasando de nuevo a RGB (esta seguira en escala de grises)
        if canal == 'blue':
            img_convertida[:, :, 1] = 0 #El canal verde se pasa a cero
            img_convertida[:, :, 2] = 0 #El canal rojo se pasa a cero
        if canal == 'green':
            img_convertida[:, :, 0] = 0 #El canal azul se pasa a cero
            img_convertida[:, :, 2] = 0 #El canal rojo se pasa a cero
        if canal == 'red':
            img_convertida[:, :, 0] = 0 #El canal azul se pasa a cero
            img_convertida[:, :, 1] = 0 #El canal verde se pasa a cero
        return img_convertida


    def makeHue(self):
        # Se convierte de BGR a HSV
        imagen_hsv = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2HSV)
        imagen_hsv[:, :, 1] = 255 #La componente en S se pasa a su valor maximo
        imagen_hsv[:, :, 2] = 255 #La componente en V se pasa a su valor maximo
        return imagen_hsv
