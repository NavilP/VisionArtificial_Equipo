import numpy as np

# Funcion para cacular la transformada
def hough_transform(image):
    hght, wid = image.shape

    # Maximo valor de distancia (rho)
    max_rho = int(np.sqrt(hght**2 + wid**2))

    # Ángulos en grados convertidos a radianes
    theta_range = np.deg2rad(np.arange(-90, 90))

    # Rango de rho
    rho_range = np.arange(-max_rho, max_rho + 1)

    # Matriz acumulativa H de tamaño de las rho*thetas
    H = np.zeros((len(rho_range), len(theta_range)), dtype=np.uint64)

    # Encontrar los pixeles que son 0 en la imagen
    white_pixels = np.argwhere(image > 0)
    #edge_pixels = np.argwhere(img > 0)

    # Transformada de Hough
    for y, x in white_pixels:
        for theta_index, theta in enumerate(theta_range):
            # Calcular rho
            rho = int(x * np.cos(theta) + y * np.sin(theta))
            rho_index = np.argmin(np.abs(rho_range - rho))
            #rho_index = np.argmin(np.abs(rho + rho_range/2))
            H[rho_index, theta_index] += 1

    return H, theta_range, rho_range

# Funcion para encontrar y dibujar las líneas detectadas en la imagen original
def hough_line_peaks(H, thetas, rhos, threshold=0.5):
    # Encontrar los picos en la matriz acumuladora H
    peak_values = np.max(H) * threshold
    peak_indices = np.argwhere(H > peak_values)
    
    # Obtener los valores de rho y theta de los picos
    rho_values = [rhos[idx[0]] for idx in peak_indices]
    theta_values = [thetas[idx[1]] for idx in peak_indices]
    
    return rho_values, theta_values