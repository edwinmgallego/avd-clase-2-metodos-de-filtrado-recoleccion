import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('iris.csv')

# Usar solo petal_length y petal_width
X = df[['petal_length', 'petal_width']]

# Modelo de K-means
kmeans = KMeans(n_clusters=3, random_state=0)
df['cluster'] = kmeans.fit_predict(X)

# Visualizar resultados
plt.scatter(X['petal_length'], X['petal_width'], c=df['cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroides')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('K-means con Iris Dataset')
plt.legend()
plt.show()
