import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Datos ficticios
data = {
    "Tamaño (m2)": [50, 60, 80, 100, 120],
    "Habitaciones": [1, 2, 2, 3, 3],
    "Precio (en miles)": [150, 200, 250, 300, 350]
}
df = pd.DataFrame(data)

# Variables independientes (X) y dependiente (Y)
X = df[["Tamaño (m2)", "Habitaciones"]]
Y = df["Precio (en miles)"]

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
df["Precio Predicho"] = Y_pred
print(df)

# Configurar la figura 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Datos
x1 = df["Tamaño (m2)"]
x2 = df["Habitaciones"]
y_actual = df["Precio (en miles)"]
y_pred = df["Precio Predicho"]

# Graficar los datos reales
ax.scatter(x1, x2, y_actual, color='blue', label='Datos Reales', s=50)

# Graficar los datos predichos
ax.scatter(x1, x2, y_pred, color='red', label='Datos Predichos', s=50)

# Etiquetas y título
ax.set_xlabel("Tamaño (m2)")
ax.set_ylabel("Habitaciones")
ax.set_zlabel("Precio (en miles)")
ax.set_title("Regresión Lineal Múltiple")

# Leyenda
ax.legend()

# Mostrar gráfica
plt.show()
