"""
    Práctica 1.2: Análisis Inicial Imagen Digital
    Vision Artificial
    Equipo:
    Miguel Angel Sanchez Zanjuampa
    Navil Pineda Rugerio
    
    No le haga caso a este archivo profe jaja
    No le haga caso a este archivo profe jaja
    No le haga caso a este archivo profe jaja
    No le haga caso a este archivo profe jaja
    No le haga caso a este archivo profe jaja
    No le haga caso a este archivo profe jaja
    No le haga caso a este archivo profe jaja
    
    El otro (.ipynb) es el bueno jeje 
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
def histograma(imagen, canal):
    hght, wid, channel = img.shape
    count =[]
    r = []
     
    for k in range(0, 255):
        r.append(k)
        count1 = 0
         
        for i in range(hght):
            for j in range(wid):
                if img[i, j, canal] == k:
                    count1+= 1
        count.append(count1)
         
    return (r, count)

r, count = histograma(np.copy(img), 0) # Canal rojo


# Funcion para tomar un fragmento de la imagen

# Funcion para convertir a escala de grises
def escala_grises(imagen):
    wid, hght, canal = imagen.shape
    matriz = np.copy(imagen)
    for i in range(hght):
        for j in range(wid):
            pixel = imagen[j][i]
            gris = (pixel[0] * 0.299) + (pixel[1] * 0.587) + (pixel[2] * 0.114)
            matriz[j][i][0] = gris
            matriz[j][i][1] = gris
            matriz[j][i][2] = gris
    return matriz
grisesImg = escala_grises(np.copy(img))
cv2.imshow('Imagen en escala de grises', grisesImg)


# Mostrar histograma

# Graficar valores de intensidad de 5 filas

cv2.waitKey(0)
cv2.destroyAllWindows()


"""# Separar las imagenes en 3 canales
B, G, R = cv2.split(original)

# Convertir cada canal en arreglo
ArrayR = np.asarray(R)
ArrayG = np.asarray(G)
ArrayB = np.asarray(B)

# Hacer las operaciones en cada arreglo para el gris preciso
for i in np.nditer(ArrayR, op_flags=['readwrite']):
    i[...] = i[...] * 0.21

for i in np.nditer(ArrayG, op_flags=['readwrite']):
    i[...] = i[...] * 0.72

for i in np.nditer(ArrayB, op_flags=['readwrite']):
    i[...] = i[...] * 0.07

# Sumar los 3 canales
suma1 = cv2.add(R, G)
suma2 = cv2.add(suma1, B)

# Guardar la imagen sumada y abrirla en 3 canales
cv2.imwrite(
    "C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Fotos/suma2.jpg", suma2)
gray = cv2.imread('Fotos/suma2.jpg', 1)

# Mostrar la imagen en gris
cv2.imshow('Imagen gris', gray)"""
