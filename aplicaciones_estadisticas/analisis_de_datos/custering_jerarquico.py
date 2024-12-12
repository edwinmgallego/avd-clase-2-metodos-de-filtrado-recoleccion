from scipy.cluster.hierarchy import dendrogram, linkage

# Generar jerarquía
Z = linkage(X, method='ward')

# Dibujar dendrograma
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title("Dendrograma de Clustering Jerárquico")
plt.show()
