#K-means (K-medias)
#Descripción: K-means es un algoritmo de agrupamiento que divide los datos en ( k ) grupos o clústeres,
# donde ( k ) es el número de clústeres definido por el usuario. El objetivo es minimizar la suma de las distancias 
# al cuadrado entre los puntos de datos y el centroide del clúster al que pertenecen.


#Ventajas:

#Fácil de implementar: El algoritmo es sencillo y directo.
#Escalable: Funciona bien con grandes conjuntos de datos.
#Limitaciones:

#Necesita definir ( k ) de antemano: El número de clústeres debe ser especificado antes de ejecutar el algoritmo.
#Sensible a valores atípicos: Los puntos de datos atípicos pueden afectar significativamente los resultados.
#Usos:

#Segmentación de clientes: Agrupar clientes con características similares.
#Análisis de imágenes: Agrupar píxeles con colores similares.

from sklearn.cluster import KMeans
import seaborn as sns

# Generar datos de ejemplo
from sklearn.datasets import make_blobs
#Se generan 300 puntos de datos distribuidos en 4 clústeres con una desviación estándar de 0.6.
# random_state=0 asegura que los datos generados sean reproducibles.
data, labels_true = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# Aplicar K-means
kmeans = KMeans(n_clusters=4)
#Se crea un modelo K-means con 4 clústeres y se ajusta a los datos generados.
kmeans.fit(data)
labels = kmeans.labels_

# Visualización
#Se dibujan los puntos de datos coloreados según el clúster al que pertenecen (c=kmeans.labels_).
#Se dibujan los centroides de los clústeres en rojo.
#Se añade un título y una leyenda para mayor claridad.
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
plt.title("Clustering con K-means")
plt.show()



#Los centroides son puntos que representan el centro de un clúster en el algoritmo K-means. Cada clúster tiene un único centroide, que es el promedio de todos los puntos de datos dentro de ese clúster. En otras palabras, el centroide es el punto que minimiza la suma de las distancias al cuadrado entre sí mismo y todos los puntos de datos en el clúster.
