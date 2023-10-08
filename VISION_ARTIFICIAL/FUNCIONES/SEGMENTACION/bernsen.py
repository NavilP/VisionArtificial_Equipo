import numpy as np

def bernsen_thresolding(image, k):
    wid, hght = image.shape
    newImage = np.copy(image)

    # Radio de la vecindad
    radius = k//2

    for i in range(radius+1, wid-radius):
        for j in range(radius+1, hght-radius):
            # Definir vecindad
            nb = image[i-radius:i+radius+1,j-radius:j+radius+1]

            # Obtener el maximo y minimo de la vecindad
            minNb = np.min(nb)
            maxNb = np.max(nb)
            
            # Valor de umbral
            tValue = (minNb + maxNb) / 2

            # Diferencia de contraste mayor en la vecindad
            difC = maxNb - minNb

            # Definir si el contraste es menor al minimo pasado como parametro
            if (difC < k):
                nClass = 255 # La vecindad completa es una clase
            else:
                nClass = tValue
            
            # Umbralizar el pixel
            if(image[i,j] < nClass):
                newImage[i,j] = 255
            else:
                newImage[i,j] = 0
    return newImage