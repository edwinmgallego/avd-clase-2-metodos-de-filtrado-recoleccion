#Regresión Lineal Múltiple
#En este ejemplo, usamos datos ficticios para predecir el precio de una casa basado en el tamaño (𝑋1)
# y el número de habitaciones (𝑋2 ).

#pandas: Para crear y manejar los datos en forma de tabla (DataFrame).
#LinearRegression: Implementa el modelo de regresión lineal múltiple.
#mean_squared_error: Calcula el error cuadrático medio para evaluar el modelo.


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Datos ficticios

# Se crea un diccionario que contiene:
#Tamaño (m²): Área de la casa.
#Habitaciones: Número de habitaciones en la casa.
#Precio (en miles): Precio de la casa en miles de dólares.
#Luego, se convierte el diccionario en un DataFrame usando pd.DataFrame.

data = {
    "Tamaño (m2)": [50, 60, 80, 100, 120],
    "Habitaciones": [1, 2, 2, 3, 3],
    "Precio (en miles)": [150, 200, 250, 300, 350]
}
df = pd.DataFrame(data)

# Variables independientes (X) y dependiente (Y)
# Variables independientes (X): "Tamaño (m2)" y "Habitaciones". Son las características que se usan para predecir.
#Variable dependiente (Y): "Precio (en miles)". Es el valor que queremos predecir.

X = df[["Tamaño (m2)", "Habitaciones"]]
Y = df["Precio (en miles)"]

# Modelo de Regresión Lineal /  Creación y entrenamiento del modelo

# Se crea una instancia del modelo de regresión lineal.
#El método fit(X, Y) entrena el modelo, ajustando los coeficientes de la ecuación
#Y=β0 +β1X1 +β2​X2​
#donde
#β0 ​ : Intercepto (precio base cuando las variables independientes son cero).
#β1,β2 : Coeficientes asociados al tamaño (𝑋1​ ) y al número de habitaciones (𝑋2 ).
model = LinearRegression()
model.fit(X, Y)

# Predicciones / Generación de predicciones
# El modelo usa los datos de entrada (X) para predecir los valores de precio (Y_pred).
Y_pred = model.predict(X)

# Coeficientes /  Coeficientes e intercepto del modelo
#Intercepto (β0): Representa el valor inicial del precio (en miles) cuando 
#𝑋1=0y 𝑋2=0.
#Coeficientes (β1, β2): Indican cuánto cambia el precio por cada unidad adicional de tamaño o número de habitaciones.
print(f"Intercepto (β0): {model.intercept_}")
print(f"Coeficientes (β1, β2): {model.coef_}")

# Evaluación del modelo
#El error cuadrático medio (MSE) mide qué tan lejos están las predicciones del modelo de los valores reales. Un MSE más bajo indica un mejor ajuste.

mse = mean_squared_error(Y, Y_pred)
print(f"Error cuadrático medio (MSE): {mse}")

# Mostrar resultados
# Se agrega una nueva columna al DataFrame con los precios predichos (Y_pred).
# Finalmente, se imprime el DataFrame actualizado para comparar los precios reales con los predichos
df["Precio Predicho"] = Y_pred
print(df)

#Resultado del modelo
#Intercepto y coeficientes:
#Estos valores pueden interpretarse así: 
# 𝛽0β0 : Precio base.
#𝛽1 : Incremento en el precio por cada m² adicional.
#𝛽2 : Incremento en el precio por cada habitación adicional.
#Error cuadrático medio (MSE):
#Evalúa qué tan bien el modelo se ajusta a los datos.

#DataFrame actualizado:
#Muestra el precio real y el precio predicho por el modelo.
