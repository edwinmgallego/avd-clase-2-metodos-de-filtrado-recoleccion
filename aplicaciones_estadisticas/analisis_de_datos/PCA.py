# Análisis de Componentes Principales (PCA)
#El PCA es una técnica estadística que se utiliza para reducir la dimensionalidad de un conjunto de datos. Esto significa que toma un conjunto de variables posiblemente correlacionadas y las transforma en un conjunto más pequeño de variables no correlacionadas llamadas componentes principales.
# Los objetivos principales del PCA son:
#Reducción de dimensionalidad: Facilita la visualización y el análisis de datos al reducir el número de dimensiones.
#Preservación de la variabilidad: Mantiene la mayor cantidad posible de la variabilidad original de los datos.
#Eliminación de ruido: Ayuda a eliminar el ruido y las redundancias en los datos.
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Generamos datos aleatorios
np.random.seed(0)
data = np.random.rand(100, 5)  # 100 muestras, 5 características

# Aplicar PCA
#Aplicación del PCA: Se crea un objeto PCA especificando que queremos reducir los datos a 2 componentes principales. Luego,
# se ajustan y transforman los datos originales con fit_transform.
pca = PCA(n_components=2)  # Reducimos a 2 componentes principales
data_pca = pca.fit_transform(data)

# Ver varianza explicada
#Varianza explicada: Se imprime la proporción de la varianza total que explica cada uno de los componentes principales. Esto nos indica cuánta información de los 
# datos originales se conserva en los componentes principales.
print("Varianza explicada por cada componente:", pca.explained_variance_ratio_)

# Visualización
plt.scatter(data_pca[:, 0], data_pca[:, 1])
plt.title("Datos reducidos con PCA")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.show()
