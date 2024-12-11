

#Introducción a la Regresión Logística para Clasificación
#La regresión logística es un modelo utilizado para resolver problemas de clasificación. 
# Su objetivo es predecir la probabilidad de que una observación pertenezca a una categoría específica (por ejemplo, 0 o 1
# en una clasificación binaria).

#La regresión logística utiliza la función sigmoide para transformar una combinación lineal de las variables de entrada en valores de probabilidad comprendidos entre 0 y 1.


#numpy (np): Para trabajar con arreglos numéricos y realizar cálculos matemáticos.
#pandas (pd): (Aunque no se utiliza aquí) Suele ser usado para manejar y analizar datos estructurados.
#train_test_split: Función de sklearn que divide los datos en conjuntos de entrenamiento y prueba.
#LogisticRegression: Implementa el modelo de Regresión Logística, utilizado aquí para clasificación binaria.
#accuracy_score y classification_report: Métricas para evaluar la calidad del modelo.


# Importar librerías
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Crear un dataset simulado
# np.random.seed(42): Fija la semilla del generador aleatorio para obtener resultados reproducibles.
#n_samples = 500: Genera un dataset con 500 muestras (filas).
#X = np.random.rand(n_samples, 2): Crea una matriz aleatoria de tamaño (500, 2), donde cada fila tiene 2 características (en este caso, valores aleatorios que representan azúcar en sangre y presión arterial).
#y: Define las etiquetas binarias (0 o 1).
#Si la suma de los valores de las dos características (X[:, 0] y X[:, 1]) es mayor que 1, la etiqueta será 1, de lo contrario será 0.
#.astype(int) convierte los valores booleanos en enteros.
np.random.seed(42)
n_samples = 500
X = np.random.rand(n_samples, 2)  # 2 características (azúcar en sangre y presión arterial)
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Etiquetas: 1 si la suma es mayor a 1, de lo contrario 0

# Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Predecir sobre los datos de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
print("Exactitud:", accuracy_score(y_test, y_pred))
print("Reporte de Clasificación:")
print(classification_report(y_test, y_pred))

#Resumen del Código
#Crea datos simulados con dos características y etiquetas binarias.
#Divide los datos en conjuntos de entrenamiento y prueba.
#Entrena un modelo de Regresión Logística.
#Predice etiquetas para el conjunto de prueba.
#Evalúa el desempeño del modelo con métricas como exactitud y reporte de clasificación.
