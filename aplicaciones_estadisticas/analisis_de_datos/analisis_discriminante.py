#Análisis Discriminante
#El análisis discriminante es una técnica de reducción de dimensionalidad que se utiliza para
# separar clases en un espacio de menor dimensión. Su objetivo principal es maximizar la separación entre las clases y minimizar la varianza dentro de cada clase. Esto se logra encontrando una combinación lineal de características
# que mejor separa las diferentes clases.

#aplicaciones
#Clasificación supervisada: Se utiliza para clasificar datos en diferentes categorías.
#Visualización de datos etiquetados: Ayuda a visualizar datos en un espacio de menor dimensión.
#Detección de patrones en datos clasificados: Identifica patrones en datos que ya están clasificados.

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris
import pandas as pd

# Cargar datos
#Se carga el conjunto de datos Iris. X contiene las características (longitud y ancho de sépalos y pétalos) y y contiene las etiquetas de las clases (las especies de iris).
iris = load_iris()
X, y = iris.data, iris.target

# Aplicar LDA
#Se crea una instancia de LinearDiscriminantAnalysis especificando que queremos reducir a 2 componentes (n_components=2). Luego, se ajusta el modelo a los datos X y y, y se transforma X a un nuevo espacio de menor dimensión X_lda.
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)

# Visualización
#Se crea un gráfico de dispersión de los datos transformados X_lda. 
# Los puntos se colorean según sus etiquetas y usando un mapa de colores (cmap='rainbow'). 
# Se añaden etiquetas y un título al gráfico.

#La varianza dentro de las clases se refiere a la medida de dispersión de los datos dentro de cada clase individual.
# En el contexto del análisis discriminante, es importante minimizar esta varianza para que los datos de cada clase 
# estén lo más agrupados posible, lo que facilita la separación entre diferentes clases.
plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y, cmap='rainbow', edgecolor='k')
plt.title("Análisis Discriminante Lineal")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.show()
