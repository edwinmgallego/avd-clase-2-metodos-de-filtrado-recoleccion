from sklearn.preprocessing import StandardScaler

# Leer archivo CSV
df = pd.read_csv('comportamiento.csv')

# Normalizar datos
X = df[['Visitas', 'Sesiones', 'Tiempo_en_Sitio', 'Productos_Visitados']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Modelo de K-means con 5 clusters
kmeans = KMeans(n_clusters=5, random_state=0)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Visualización (2 primeras dimensiones)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=df['cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroides')
plt.xlabel('Visitas (Normalizado)')
plt.ylabel('Sesiones (Normalizado)')
plt.title('K-means en Comportamiento de Usuarios')
plt.legend()
plt.show()
