from sklearn.cluster import DBSCAN

# Modelo DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)

# Visualizar clústeres
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='plasma')
plt.title("Clústeres con DBSCAN")
plt.show()
