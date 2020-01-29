# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:32:58 2019

@author: fraal
"""

from PIL import Image
import time

def abrir_imagen(im):
    tiempoIn = time.time();
    ruta = ("C:/Users/fraal/Desktop/PythonImagesProces/" + im) 
    im = Image.open(ruta)
    im.show()
    tiempoFin = time.time();
    print('El proceso tardo: ', tiempoFin- tiempoIn, 'Segundos')
    


def escala_grises(im):
    tiempoIn = time.time();
    ruta = ("C:/Users/fraal/Desktop/PythonImagesProces/" + im) 
    im = Image.open(ruta)
    im.show()
    im2 = im
    i = 0
    while i < im2.size[0]:
        j = 0
        while j < im2.size[1]:
            r, g, b = im2.getpixel((i,j))
            g = (r+g+b)/3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            im2.putpixel((i,j),pixel)
            j+=1
        i+=1
    im2.show()
    tiempoFin = time.time();
    print('El proceso tardo: ', tiempoFin- tiempoIn, 'Segundos')
    
    
    
    
def maximo(im):
    tiempoIn = time.time();
    ruta = ("C:/Users/fraal/Desktop/PythonImagesProces/" + im) 
    im = Image.open(ruta)
    im.show()
    im3 = im
    i = 0
    while i < im3.size[0]:
        j = 0
        while j < im3.size[1]:
            maximo = max(im3.getpixel((i,j)))
            pixel = tuple([maximo,maximo,maximo])
            im3.putpixel((i,j), pixel)
            j+=1
        i+=1
        print("El nivel maximo de gris es: ", maximo)
        im3.show()
        tiempoFin = time.time();
        print('El proceso tardo: ', tiempoFin- tiempoIn, 'Segundos')
        
        
        
        
        
        
    