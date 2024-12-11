#Problema: Clasificación de frutas (manzanas y naranjas) basado en características simples como peso y color.

#Dataset: Crear datos sintéticos con pandas.
#Modelo: Usar LogisticRegression de sklearn.
#Evaluación: Calcular precisión y recall.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np

# Crear un dataset simple
data = {
    'peso': [150, 160, 140, 170, 130, 180, 155, 165],
    'color': [1, 1, 1, 1, 0, 0, 0, 0],  # 1: Manzana, 0: Naranja
    'fruta': [1, 1, 1, 1, 0, 0, 0, 0]  # 1: Manzana, 0: Naranja
}
df = pd.DataFrame(data)

# Dividir datos en características (X) y etiqueta (y)
X = df[['peso', 'color']]
y = df['fruta']

# Dividir el conjunto en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Predicción y evaluación
y_pred = model.predict(X_test)

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Puntos de datos
colors = ['red' if label == 1 else 'orange' for label in y]
plt.scatter(X['peso'], X['color'], c=colors, label='Datos originales', edgecolor='k')

# Recta de decisión
x_values = np.linspace(X['peso'].min(), X['peso'].max(), 100)
y_values = -(model.coef_[0][0] * x_values + model.intercept_[0]) / model.coef_[0][1]
plt.plot(x_values, y_values, label='Línea de decisión', color='blue', linewidth=2)

# Etiquetas y leyenda
plt.xlabel('Peso (g)')
plt.ylabel('Color (1: Manzana, 0: Naranja)')
plt.title('Clasificación de Frutas con Regresión Logística')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()

# Mostrar resultados
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
print("Precisión:", accuracy)
print("Reporte de Clasificación:\n", classification_rep)


#Dataset: Contiene los datos sintéticos de frutas (manzanas y naranjas) con características de peso y color para entrenar el modelo.
#Modelo de Regresión Logística: Se entrena utilizando el método fit() de LogisticRegression y se predicen los valores con predict().
#Visualización: Se muestra un gráfico de dispersión de los puntos de datos y la línea de decisión generada por el modelo.
# Los colores de los puntos indican las frutas (rojo para manzanas y naranja para naranjas).
#Evaluación: Muestra la precisión y el reporte de clasificación con métricas como precisión, recall y f1-score.
