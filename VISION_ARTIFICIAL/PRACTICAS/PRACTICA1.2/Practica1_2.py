"""
    Práctica 1.2: Análisis Inicial Imagen Digital
    Vision Artificial
    Equipo:
    Miguel Angel Sanchez Zanjuampa
    Navil Pineda Rugerio
"""

# Librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Abrir imagen
ruta = 'VISION_ARTIFICIAL/IMAGES/ldscp.jpg'
img = cv2.imread(ruta, 1)
cv2.imshow('Imagen Original', img)

# Funcion para histograma de imagen

# Funcion para convertir a escala de grises

# Mostrar histograma

# Graficar valores de intensidad de 5 filas

cv2.waitKey(0)
cv2.destroyAllWindows()
