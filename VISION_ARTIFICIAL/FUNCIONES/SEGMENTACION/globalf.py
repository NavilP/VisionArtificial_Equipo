import numpy as np

# Recibe una imagen y un valor de umbral
def glob(img,valor):
    
    forma = np.shape(img)
    base = np.zeros(forma)
    
    alto, ancho = forma
    
    for i in range(alto):
        for j in range(ancho):
            if(img[i][j] <= valor):
                base[i][j] = 0
            else:
                base[i][j] = 1
    
    return base

def global_thresholding(img, umbral):
    wid, hght = img.shape
    newImage = np.empty((wid,hght))
    
    for i in range(wid):
        for j in range(hght):
            if img[i,j] > umbral:
                newImage[i][j] = 0
            else:
                newImage[i][j] = 255
            
    return newImage