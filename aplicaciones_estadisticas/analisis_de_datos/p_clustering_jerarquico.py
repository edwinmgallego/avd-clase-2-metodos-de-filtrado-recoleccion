from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Leer archivo CSV
df = pd.read_csv('iris.csv')

# Usar petal_length y petal_width
X = df[['petal_length', 'petal_width']]

# Clustering jerárquico
hc = linkage(X, method='ward')
dendrogram(hc)
plt.title('Dendrograma - Iris Dataset')
plt.xlabel('Flores')
plt.ylabel('Distancia Euclidiana')
plt.show()

# Modelo
model = AgglomerativeClustering(n_clusters=3)
df['cluster'] = model.fit_predict(X)

# Visualizar clusters
plt.scatter(X['petal_length'], X['petal_width'], c=df['cluster'], cmap='viridis')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Clustering Jerárquico en Iris Dataset')
plt.show()
