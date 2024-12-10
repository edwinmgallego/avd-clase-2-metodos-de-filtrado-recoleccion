# Predicción del Salario de Empleados
#Supongamos que tenemos un archivo empleados.csv con las siguientes columnas:

#Años de Experiencia
#Nivel de Educación (1: Secundaria, 2: Licenciatura, 3: Maestría, 4: Doctorado)
#Salario (en miles de dólares)
#El objetivo es predecir el salario de los empleados basado en sus años de experiencia y nivel de educación.

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar los datos desde un archivo CSV
df = pd.read_csv('empleados.csv')

# Variables independientes (X) y dependiente (Y)
X = df[["Años de Experiencia", "Nivel de Educación"]]
Y = df["Salario"]

# Modelo de Regresión Lineal
model = LinearRegression()
model.fit(X, Y)

# Predicciones
Y_pred = model.predict(X)

# Coeficientes
print(f"Intercepto (β0): {model.intercept_}")
print(f"Coeficientes (β1, β2): {model.coef_}")

# Evaluación del modelo
mse = mean_squared_error(Y, Y_pred)
print(f"Error cuadrático medio (MSE): {mse}")

# Agregar las predicciones al DataFrame
df["Salario Predicho"] = Y_pred
print(df)

# Configurar la figura 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Datos
x1 = df["Años de Experiencia"]
x2 = df["Nivel de Educación"]
y_actual = df["Salario"]
y_pred = df["Salario Predicho"]

# Graficar los datos reales
ax.scatter(x1, x2, y_actual, color='blue', label='Datos Reales', s=50)

# Graficar los datos predichos
ax.scatter(x1, x2, y_pred, color='red', label='Datos Predichos', s=50)

# Etiquetas y título
ax.set_xlabel("Años de Experiencia")
ax.set_ylabel("Nivel de Educación")
ax.set_zlabel("Salario (en miles)")
ax.set_title("Predicción del Salario de Empleados")

# Leyenda
ax.legend()

# Mostrar gráfica
plt.show()

#Resumen
#Importar bibliotecas: Necesarias para el análisis y visualización.
#Cargar datos: Desde un archivo CSV.
#Definir variables: Independientes y dependiente.
#Crear y entrenar el modelo: Usando LinearRegression.
#Realizar predicciones: Con el modelo entrenado.
#Obtener coeficientes: Del modelo.
#Evaluar el modelo: Con el MSE.
#Agregar predicciones: Al DataFrame.
#Visualizar resultados: En una gráfica 3D.