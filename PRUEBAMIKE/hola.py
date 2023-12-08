import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Función de regresión no lineal a*x^b
def nonlinear_function(x, a, b):
    return a * np.power(x, b)

# Datos de ejemplo
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 8, 18, 32, 50])

# Ajuste de la curva a los datos
params, covariance = curve_fit(nonlinear_function, x_data, y_data)

# Parámetros óptimos
a_optimal, b_optimal = params

# Generar puntos predichos con la función ajustada
y_pred = nonlinear_function(x_data, a_optimal, b_optimal)

# Gráfico de los datos y la regresión no lineal
plt.scatter(x_data, y_data, label='Datos reales')
plt.plot(x_data, y_pred, label=f'Regresión no lineal: {a_optimal:.2f} * x^{b_optimal:.2f}', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()