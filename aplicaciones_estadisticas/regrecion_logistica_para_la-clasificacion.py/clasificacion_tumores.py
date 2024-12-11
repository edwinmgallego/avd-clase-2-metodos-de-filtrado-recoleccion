from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Cargar dataset
#Se carga el conjunto de datos de cáncer de mama, donde X contiene las características y y las etiquetas (0 para benigno y 1 para maligno).
data = load_breast_cancer()
X, y = data['data'], data['target']

# PCA para reducción de dimensionalidad

#Se aplica PCA (Análisis de Componentes Principales) para reducir las dimensiones de los datos a 5 componentes principales, lo que ayuda a simplificar el modelo y reducir el ruido.
#

pca = PCA(n_components=5)
X_reduced = pca.fit_transform(X)

# Dividir datos
# Se dividen los datos en conjuntos de entrenamiento (70%) y prueba (30%).
X_train, X_test, y_train, y_test = train_test_split(X_reduced, y, test_size=0.3, random_state=42)

# Entrenamiento del Modelo
# Se entrena un modelo de regresión logística con los datos de entrenamiento. max_iter=1000 establece el número máximo de iteraciones para el algoritmo de optimización.
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluación
# Se predicen las etiquetas para los datos de prueba y se imprime un reporte de clasificación que incluye métricas como precisión, recall y F1-score.
y_pred = model.predict(X_test)
print("Reporte de Clasificación:\n", classification_report(y_test, y_pred))
