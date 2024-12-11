# Importar librerías
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Fijar semilla para reproducibilidad
np.random.seed(42)

# Crear un dataset simulado
n_samples = 500  # Cantidad de pacientes
glucosa = np.random.uniform(70, 200, n_samples)  # Niveles de glucosa (mg/dL)
presion = np.random.uniform(50, 120, n_samples)  # Presión arterial (mmHg)
# Etiqueta: 1 si glucosa + presión > 220, de lo contrario 0
diabetes = ((glucosa + presion) > 220).astype(int)

# Crear el DataFrame
data = pd.DataFrame({
    "Glucosa (mg/dL)": glucosa,
    "Presión Arterial (mmHg)": presion,
    "Diabetes (1=Sí, 0=No)": diabetes
})

# Dividir en características (X) y etiquetas (y)
X = data[["Glucosa (mg/dL)", "Presión Arterial (mmHg)"]]
y = data["Diabetes (1=Sí, 0=No)"]

# Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Predecir sobre los datos de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
print("Resultados del Modelo:")
print("Exactitud:", accuracy_score(y_test, y_pred))
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

# Crear una gráfica de resultados
plt.figure(figsize=(10, 6))

# Obtener datos correctamente clasificados y errores
correct = (y_test == y_pred)
incorrect = (y_test != y_pred)

# Graficar datos correctamente clasificados
plt.scatter(
    X_test[correct]["Glucosa (mg/dL)"], 
    X_test[correct]["Presión Arterial (mmHg)"], 
    c='green', label='Correcto (Predicción)', alpha=0.6
)

# Graficar datos clasificados incorrectamente
plt.scatter(
    X_test[incorrect]["Glucosa (mg/dL)"], 
    X_test[incorrect]["Presión Arterial (mmHg)"], 
    c='red', label='Incorrecto (Predicción)', alpha=0.6
)

# Etiquetas y configuración de la gráfica
plt.title("Resultados de la Clasificación: Diabetes", fontsize=14)
plt.xlabel("Glucosa (mg/dL)", fontsize=12)
plt.ylabel("Presión Arterial (mmHg)", fontsize=12)
plt.axhline(y=120, color='black', linestyle='--', linewidth=0.8, alpha=0.7)  # Línea de guía para presión
plt.axvline(x=200, color='black', linestyle='--', linewidth=0.8, alpha=0.7)  # Línea de guía para glucosa
plt.legend()
plt.grid(alpha=0.3)
plt.show()
