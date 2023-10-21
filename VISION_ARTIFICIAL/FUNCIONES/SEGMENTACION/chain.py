import numpy as np
import cv2

def minimum_magnitude(cadena):
    dim = cadena.shape[0]
    nuevaCadena = np.zeros_like(cadena)
    for i in range(dim):
        if cadena[i] == 0:
            if cadena[i + 1] == 0:
                if cadena[i + 2] == 0 or cadena[i + 2] == 1:
                    nuevaCadena[0 : dim - i] = cadena[i:]
                    nuevaCadena[dim - i :] = cadena[0:i]
                    break
    return nuevaCadena

def first_difference(cadena, connect):
    distance = np.zeros_like(cadena)
    if connect == 4:
        # Distancia segun los numeros
        zero_dis =  [0,3,2,1]
        one_dis =   [1,0,3,2]
        two_dis =   [2,1,0,3]
        three_dis = [3,2,1,0]

        for i in range(cadena.shape[0]):
            if(i<cadena.shape[0]-1):
                if cadena[i+1] == 0:
                    distance[i] = zero_dis[cadena[i]]
                if cadena[i+1] == 1:
                    distance[i] = one_dis[cadena[i]]
                if cadena[i+1] == 2:
                    distance[i] = two_dis[cadena[i]]
                if cadena[i+1] == 3:
                    distance[i] = three_dis[cadena[i]]
            else:
                if cadena[0] == 0:
                    distance[i] = zero_dis[cadena[i]]
                if cadena[0] == 1:
                    distance[i] = one_dis[cadena[i]]
                if cadena[0] == 2:
                    distance[i] = two_dis[cadena[i]]
                if cadena[0] == 3:
                    distance[i] = three_dis[cadena[i]]
    if connect == 8:
            # Distancia segun los numeros
            zero_dis =  [0,7,6,5,4,3,2,1]
            one_dis =   [1,0,7,6,5,4,3,2]
            two_dis =   [2,1,0,7,6,5,4,3]
            three_dis = [3,2,1,0,7,6,5,4]
            four_dis =  [4,3,2,1,0,7,6,5]
            five_dis =  [5,4,3,2,1,0,7,6]
            six_dis =   [6,5,4,3,2,1,0,7]
            seven_dis = [7,6,5,4,3,2,1,0]

            for i in range(cadena.shape[0]):
                if(i<cadena.shape[0]-1):
                    if cadena[i+1] == 0:
                        distance[i] = zero_dis[cadena[i]]
                    if cadena[i+1] == 1:
                        distance[i] = one_dis[cadena[i]]
                    if cadena[i+1] == 2:
                        distance[i] = two_dis[cadena[i]]
                    if cadena[i+1] == 3:
                        distance[i] = three_dis[cadena[i]]
                    if cadena[i+1] == 4:
                        distance[i] = four_dis[cadena[i]]
                    if cadena[i+1] == 5:
                        distance[i] = five_dis[cadena[i]]
                    if cadena[i+1] == 6:
                        distance[i] = six_dis[cadena[i]]
                    if cadena[i+1] == 7:
                        distance[i] = seven_dis[cadena[i]]
                else:
                    if cadena[0] == 0:
                        distance[i] = zero_dis[cadena[i]]
                    if cadena[0] == 1:
                        distance[i] = one_dis[cadena[i]]
                    if cadena[0] == 2:
                        distance[i] = two_dis[cadena[i]]
                    if cadena[0] == 3:
                        distance[i] = three_dis[cadena[i]]
                    if cadena[i] == 4:
                        distance[i] = four_dis[cadena[i]]
                    if cadena[i] == 5:
                        distance[i] = five_dis[cadena[i]]
                    if cadena[i] == 6:
                        distance[i] = six_dis[cadena[i]]
                    if cadena[i] == 7:
                        distance[i] = seven_dis[cadena[i]]
    return distance


# Función que recibe como parámetro una imagen en escala de grises y regresa su borde (como imagen) y lista de direcciones con conectividad 8
def MooreFree8(circle):
    
    ############################### Binarizar #####################################
    # Binarizacion
    _, imgBin = cv2.threshold(circle, 90, 255, cv2.THRESH_BINARY)
    # Inversa de binaria
    for i in np.nditer(imgBin, op_flags=['readwrite']):
        i[...] = 255 - i

    # Erosion(1), dilatacion(2) para eliminar ruido
    kernel = np.ones((5,5), np.uint8)
    img_erosion = cv2.erode(imgBin, kernel, iterations=1)
    test1 = cv2.dilate(img_erosion, kernel, iterations=2)
    
    ###################################### Punto de inicio y punto final #####################
    # Obtener dimensiones de la imagen
    dimensiones = test1.shape

    #print("1", test1.shape)
    
    # Concatenar con una fila mas
    nfila = np.ones((1,dimensiones[1]))
    test = np.concatenate((test1, nfila))
    ncolumna = np.ones((dimensiones[0]+1,1))
    test = np.concatenate((test, ncolumna), axis=1)
    
    #print("2", test.shape)

    tupla = ()
    # Encontrar el valor inicial
    for i in range (dimensiones[0]):
        for j in range (dimensiones[1]):
            if test[i][j] == 0:
                tupla = (i,j)
                break
        else:
            continue
        break

    # Encontrar punto final (en sentido antihorario desde el punto de inicio8)
    end = 0
    final = ()
    while end == 0:
        
        # Izquierda abajo
        fil = tupla[0] + (1)
        col = tupla[1] + (-1)
        if test[fil, col] == 0:
            final = fil, col
            end = 1
            break

        # Abajo
        fil = tupla[0] + (1)
        col = tupla[1] + (0)
        if test[fil, col] == 0:
            final = fil, col
            end = 1
            break

        # Derecha abajo
        fil = tupla[0] + (1)
        col = tupla[1] + (1)
        if test[fil, col] == 0:
            final = fil, col
            end = 1
            break
    
    ######################################## Moore y freeman #########################################
    # Obtener dimensiones de la imagen
    dimensiones = test.shape
    
    # funcion8 que indica direccion
    funcion8 = 1

    # Nueva imagen llena de 0's para dibujar borde
    base8 = np.zeros(dimensiones)

    # Lista que guarda direcciones8
    direcciones8 = []

    # Inicializacion
    inicio = tupla

    # Pintar el primer punto (inicio) como parte del borde
    base8[inicio] = 255

    # Nuevo inicio (el que se ira recorriendo)
    ninicio8 = inicio

    # Mientras el nuevo inicio (punto actual) sea diferente del punto final (condicion de paro: Cuando se haya llegado al punto final)
    while ninicio8 != final:
        
        # Imprimir punto actual
        #print(ninicio8)
        
        
        if funcion8 == 1:
            
            # Derecha arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (1)
            val = 1
            if test[fil, col] == 0:
                direcciones8.append(val)
                ninicio8 = fil, col
                base8[ninicio8] = 255
                #print(val)
                funcion8 = 8
                continue
            
            # Derecha
            fil = ninicio8[0] + (0)
            col = ninicio8[1] + (1)
            val = 0
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 1
                continue
                
            # Derecha abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (1)
            val = 7
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 2
                continue
                
            # Abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (0)
            val = 6
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 3
                continue
                
            # Izquierda abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (-1)
            val = 5
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 4
                continue
            
            
        if funcion8 == 2:
            
            # Derecha arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (1)
            val = 1
            if test[fil, col] == 0:
                direcciones8.append(val)
                ninicio8 = fil, col
                base8[ninicio8] = 255
                #print(val)
                funcion8 = 8
                continue
            
            # Derecha
            fil = ninicio8[0] + (0)
            col = ninicio8[1] + (1)
            val = 0
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 1
                continue
                
            # Derecha abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (1)
            val = 7
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 2
                continue
                
            # Abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (0)
            val = 6
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 3
                continue
                
            # Izquierda abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (-1)
            val = 5
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 4
                continue

            # Izquierda
            fil = ninicio8[0] + (0)
            col = ninicio8[1] + (-1)
            val = 4
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 5
                continue
            
            
        if funcion8 == 3:
            
            # Derecha abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (1)
            val = 7
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 2
                continue
                
            # Abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (0)
            val = 6
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 3
                continue
                
            # Izquierda abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (-1)
            val = 5
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 4
                continue

            # Izquierda
            fil = ninicio8[0] + (0)
            col = ninicio8[1] + (-1)
            val = 4
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 5
                continue

            # Izquierda arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (-1)
            val = 3
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 6
                continue
            
            
        if funcion8 == 4:
            
            # Derecha abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (1)
            val = 7
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 2
                continue
                
            # Abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (0)
            val = 6
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 3
                continue
                
            # Izquierda abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (-1)
            val = 5
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 4
                continue

            # Izquierda
            fil = ninicio8[0] + (0)
            col = ninicio8[1] + (-1)
            val = 4
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 5
                continue

            # Izquierda arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (-1)
            val = 3
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 6
                continue

            # Arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (0)
            val = 2
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 7
                continue
            
            
        if funcion8 == 5:
            
            # Izquierda abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (-1)
            val = 5
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 4
                continue

            # Izquierda
            fil = ninicio8[0] + (0)
            col = ninicio8[1] + (-1)
            val = 4
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 5
                continue

            # Izquierda arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (-1)
            val = 3
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 6
                continue

            # Arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (0)
            val = 2
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 7
                continue

            # Derecha arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (1)
            val = 1
            if test[fil, col] == 0:
                direcciones8.append(val)
                ninicio8 = fil, col
                base8[ninicio8] = 255
                #print(val)
                funcion8 = 8
                continue
            
            
        if funcion8 == 6:
            
            # Izquierda abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (-1)
            val = 5
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 4
                continue

            # Izquierda
            fil = ninicio8[0] + (0)
            col = ninicio8[1] + (-1)
            val = 4
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 5
                continue

            # Izquierda arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (-1)
            val = 3
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 6
                continue

            # Arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (0)
            val = 2
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 7
                continue

            # Derecha arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (1)
            val = 1
            if test[fil, col] == 0:
                direcciones8.append(val)
                ninicio8 = fil, col
                base8[ninicio8] = 255
                #print(val)
                funcion8 = 8
                continue
            
            # Derecha
            fil = ninicio8[0] + (0)
            col = ninicio8[1] + (1)
            val = 0
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 1
                continue
            
            
        if funcion8 == 7:
            
            # Izquierda arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (-1)
            val = 3
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 6
                continue

            # Arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (0)
            val = 2
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 7
                continue

            # Derecha arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (1)
            val = 1
            if test[fil, col] == 0:
                direcciones8.append(val)
                ninicio8 = fil, col
                base8[ninicio8] = 255
                #print(val)
                funcion8 = 8
                continue
            
            # Derecha
            fil = ninicio8[0] + (0)
            col = ninicio8[1] + (1)
            val = 0
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 1
                continue
                
            # Derecha abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (1)
            val = 7
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 2
                continue
            
            
        if funcion8 == 8:
            
            # Izquierda arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (-1)
            val = 3
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 6
                continue

            # Arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (0)
            val = 2
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 7
                continue

            # Derecha arriba
            fil = ninicio8[0] + (-1)
            col = ninicio8[1] + (1)
            val = 1
            if test[fil, col] == 0:
                direcciones8.append(val)
                ninicio8 = fil, col
                base8[ninicio8] = 255
                #print(val)
                funcion8 = 8
                continue
            
            # Derecha
            fil = ninicio8[0] + (0)
            col = ninicio8[1] + (1)
            val = 0
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 1
                continue
                
            # Derecha abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (1)
            val = 7
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 2
                continue
                
            # Abajo
            fil = ninicio8[0] + (1)
            col = ninicio8[1] + (0)
            val = 6
            if test[fil, col] == 0:
                direcciones8.append(val)
                base8[fil, col] = 255
                ninicio8 = fil, col
                #print(val)
                funcion8 = 3
                continue
            
    return base8, direcciones8

# Funcion que recibe una imagen en escala de grises y regresa una imagen de su borde y la lista de direcciones en conectividad 4
def MooreFree4(circle):
    
    ############################### Binarizar #####################################
    # Binarizacion
    _, imgBin = cv2.threshold(circle, 90, 255, cv2.THRESH_BINARY)
    # Inversa de binaria
    for i in np.nditer(imgBin, op_flags=['readwrite']):
        i[...] = 255 - i

    # Erosion(1), dilatacion(2) para eliminar ruido
    kernel = np.ones((5,5), np.uint8)
    img_erosion = cv2.erode(imgBin, kernel, iterations=1)
    test1 = cv2.dilate(img_erosion, kernel, iterations=2)
    
    ###################################### Punto de inicio y punto final #####################
    # Obtener dimensiones de la imagen
    dimensiones = test1.shape

    # Concatenar con una fila mas
    nfila = np.ones((1,dimensiones[1]))
    test = np.concatenate((test1, nfila))

    tupla = ()
    # Encontrar el valor inicial
    for i in range (dimensiones[0]):
        for j in range (dimensiones[1]):
            if test[i][j] == 0:
                tupla = (i,j)
                break
        else:
            continue
        break

    # Encontrar punto final (en sentido antihorario desde el punto de inicio8)
    end = 0
    final = ()
    while end == 0:
        
        # Izquierda abajo
        fil = tupla[0] + (1)
        col = tupla[1] + (-1)
        if test[fil, col] == 0:
            final = fil, col
            end = 1
            break

        # Abajo
        fil = tupla[0] + (1)
        col = tupla[1] + (0)
        if test[fil, col] == 0:
            final = fil, col
            end = 1
            break

        # Derecha abajo
        fil = tupla[0] + (1)
        col = tupla[1] + (1)
        if test[fil, col] == 0:
            final = fil, col
            end = 1
            break
    
    ######################################## Moore y freeman #########################################
    # Obtener dimensiones de la imagen
    dimensiones = test.shape
    
    # funcion4 que indica direccion
    funcion4 = 1

    # Nueva imagen llena de 0's para dibujar borde
    base4 = np.zeros(dimensiones)

    # Lista que guarda direcciones8
    direcciones4 = []

    # Inicializacion
    start = tupla

    # Pintar el primer punto (inicio) como parte del borde
    base4[start] = 255

    # Nuevo inicio (el que se ira recorriendo)
    ninicio4 = start

    # Mientras el nuevo inicio (punto actual) sea diferente del punto final (condicion de paro: Cuando se haya llegado al punto final)
    while ninicio4 != final:
        
        # Imprimir punto actual
        #print(ninicio4)
        
        
        if funcion4 == 1:
            
            # Arriba
            fil = ninicio4[0] + (-1)
            col = ninicio4[1] + (0)
            val = 1
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 2
                continue
            
            # Derecha
            fil = ninicio4[0] + (0)
            col = ninicio4[1] + (1)
            val = 0
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 1
                continue
            
            # Abajo
            fil = ninicio4[0] + (1)
            col = ninicio4[1] + (0)
            val = 3
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 3
                continue
            
            # Izquierda
            fil = ninicio4[0] + (0)
            col = ninicio4[1] + (-1)
            val = 2
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 4
                continue
            
            
        if funcion4 == 2:
            
            # Izquierda
            fil = ninicio4[0] + (0)
            col = ninicio4[1] + (-1)
            val = 2
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 4
                continue
            
            # Arriba
            fil = ninicio4[0] + (-1)
            col = ninicio4[1] + (0)
            val = 1
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 2
                continue
            
            # Derecha
            fil = ninicio4[0] + (0)
            col = ninicio4[1] + (1)
            val = 0
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 1
                continue
            
            # Abajo
            fil = ninicio4[0] + (1)
            col = ninicio4[1] + (0)
            val = 3
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 3
                continue
            
            
        if funcion4 == 3:
            
            # Derecha
            fil = ninicio4[0] + (0)
            col = ninicio4[1] + (1)
            val = 0
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 1
                continue
            
            # Abajo
            fil = ninicio4[0] + (1)
            col = ninicio4[1] + (0)
            val = 3
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 3
                continue
            
            # Izquierda
            fil = ninicio4[0] + (0)
            col = ninicio4[1] + (-1)
            val = 2
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 4
                continue
            
            # Arriba
            fil = ninicio4[0] + (-1)
            col = ninicio4[1] + (0)
            val = 1
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 2
                continue
            
            
        if funcion4 == 4:
            
            # Abajo
            fil = ninicio4[0] + (1)
            col = ninicio4[1] + (0)
            val = 3
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 3
                continue
            
            # Izquierda
            fil = ninicio4[0] + (0)
            col = ninicio4[1] + (-1)
            val = 2
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 4
                continue
            
            # Arriba
            fil = ninicio4[0] + (-1)
            col = ninicio4[1] + (0)
            val = 1
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 2
                continue
            
            # Derecha
            fil = ninicio4[0] + (0)
            col = ninicio4[1] + (1)
            val = 0
            if test[fil, col] == 0:
                direcciones4.append(val)
                base4[fil, col] = 255
                ninicio4 = fil, col
                #print(val)
                funcion4 = 1
                continue
    
    return base4, direcciones4 