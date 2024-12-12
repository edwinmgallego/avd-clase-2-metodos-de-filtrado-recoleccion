# Leer archivo CSV
df = pd.read_csv('clientes.csv')

# Usar Edad e Ingresos_Ganados como características
X = df[['Edad', 'Ingresos_Ganados']]

# Aplicar K-means con 4 clusters
kmeans = KMeans(n_clusters=4, random_state=0)
df['cluster'] = kmeans.fit_predict(X)

# Visualizar resultados
plt.scatter(X['Edad'], X['Ingresos_Ganados'], c=df['cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroides')
plt.xlabel('Edad')
plt.ylabel('Ingresos Ganados')
plt.title('K-means en Datos Demográficos')
plt.legend()
plt.show()
