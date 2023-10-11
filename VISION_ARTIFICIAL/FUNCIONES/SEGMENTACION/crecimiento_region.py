import numpy as np
# Segmentacion por crecimiento de region
def seg_region(image, seed, threshold):
    wid, hght = image.shape
    #newImage = np.zeros((wid, hght), dtype=np.uint8)
    newImage = np.full((wid, hght), -1)

    # Punto semilla
    stack = [seed]
    val_seed = image[seed[0], seed[1]]
    val_seed = np.clip(val_seed, 0, 255)

    # Coordenadas de los 8 vecinos
    # Esquina superior izquierda, arriba, esquina superior izquierda, izquierda, derecha, esquina inferior izquierda,
    # abajo, esquina inferior derecha
    neighbours = [(-1,-1), (-1, 0), (-1, 1), (0,-1), (0, 1), (1,-1), (1,0), (1,1)]

    while stack:
        x, y = stack.pop()

        if newImage[x,y] == -1:
            actual = image[x,y]
            actual = np.clip(actual, 0, 255)
            # Si cumple con ser menor que el umbral es decir cumple con el criterio de la region
            if np.abs(actual - val_seed) <= threshold:
                newImage[x,y] = actual

                # Guarda toda la region
                # Encontrar vecinos
                for i, j in neighbours:
                    val_x, val_y = x + i, y + j
                    if val_x > 0 and val_x < wid and val_y > 0 and val_y < hght:
                        vals = (val_x, val_y)
                        stack.append(vals)
    newImage = np.where(newImage==-1, 0, newImage)
    return newImage