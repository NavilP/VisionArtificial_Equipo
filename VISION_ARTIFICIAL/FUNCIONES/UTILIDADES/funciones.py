import numpy as np

# Convolucion para detectar bordes
def convolucion(img, param):
    if param == 'sobel_x':
        kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    elif param == 'sobel_y':
        kernel = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])

    forma = np.shape(img)
    base2 = np.zeros(forma)

    for x in list(range(1, forma[0]-1)):
        for y in list(range(1, forma[1]-1)):
            suma = 0
            for i in list(range(-1, 2)):
                for j in list(range(-1, 2)):
                    suma = img[x-i, y-j] * kernel[i+1, j+1]+suma
            base2[x, y] = suma
    return base2

# Suavizado gaussiano
def suavizado(img):
    gauss = [
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 6, 4, 1]
    ]

    # Dividir el kernel entre la suma (256)
    gauss2 = np.divide(gauss, 256)

    forma = np.shape(img)
    gaussiano2 = np.zeros(forma)

    # Suavizado gaussiano
    for x in list(range(1, forma[0]-1)):
        for y in list(range(1, forma[1]-1)):
            suma = 0
            for i in list(range(-1, 2)):
                for j in list(range(-1, 2)):
                    suma = img[x-i, y-j] * gauss2[i+1, j+1]+suma
            gaussiano2[x, y] = suma
    maxs = np.max(gaussiano2)
    gaussiano2 = gaussiano2*255/maxs
    gaussiano2 = gaussiano2.astype(np.uint8)
    return gaussiano2