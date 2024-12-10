#numpy: Se utiliza para manejar y operar con matrices y arreglos de números.
#matplotlib.pyplot: Sirve para crear gráficos y visualizaciones.
#sklearn.linear_model.LinearRegression: Es el modelo de regresión lineal de scikit-learn, que ajusta una línea a los datos.
#sklearn.metrics.mean_squared_error: Permite calcular el error cuadrático medio (MSE), una métrica para evaluar el modelo.


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


#X: Representa los valores de entrada (en este caso, la inversión en publicidad).
#La función .reshape(-1, 1) convierte el arreglo de 1D en una matriz de 2D con una columna, porque scikit-learn requiere que las entradas sean matrices.
#Y: Representa los valores de salida (en este caso, las ventas generadas).

# Datos ficticios
X = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)  # Inversión en publicidad
Y = np.array([15, 30, 45, 60, 75])  # Ventas

# Modelo de Regresión Lineal
#model = LinearRegression(): Crea un modelo de regresión lineal.
#model.fit(X, Y): Ajusta (entrena) el modelo con los datos de entrada X y salida Y. 
# Este proceso calcula los coeficientes de la ecuación de la recta:

model = LinearRegression()
model.fit(X, Y)

# Predicciones

#model.predict(X): Utiliza el modelo ajustado para predecir los valores de  𝑌
#en base a los datos de  X.

Y_pred = model.predict(X)

# Coeficientes


#model.intercept_: Muestra el intercepto (𝛽0 ).
#model.coef_: Devuelve un arreglo con los coeficientes (𝛽1 ). Como hay solo un predictor, se toma el primer elemento (model.coef_[0]).


print(f"Intercepto (β0): {model.intercept_}")
print(f"Coeficiente (β1): {model.coef_[0]}")

# Evaluación del modelo

#mean_squared_error(Y, Y_pred): Calcula el error cuadrático medio (MSE).
# Es una medida de qué tan bien el modelo predice los datos reales

#
mse = mean_squared_error(Y, Y_pred)
print(f"Error cuadrático medio (MSE): {mse}")

# Gráfica

#plt.scatter(X, Y): Dibuja un gráfico de dispersión con los datos reales (puntos azules).
#plt.plot(X, Y_pred): Dibuja la línea de regresión (roja) usando las predicciones.
#plt.xlabel y plt.ylabel: Etiquetan los ejes del gráfico.
#plt.legend(): Agrega una leyenda para distinguir entre los datos reales y la línea de regresión.
#plt.show(): Muestra el gráfico


plt.scatter(X, Y, color='blue', label='Datos reales')
plt.plot(X, Y_pred, color='red', label='Regresión lineal')
plt.xlabel("Inversión en publicidad")
plt.ylabel("Ventas")
plt.legend()
plt.show()
