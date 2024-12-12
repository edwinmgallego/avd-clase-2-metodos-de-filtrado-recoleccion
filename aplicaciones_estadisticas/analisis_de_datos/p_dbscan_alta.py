# Leer archivo CSV
df = pd.read_csv('comportamiento.csv')

# Normalizar datos
X = df[['Visitas', 'Sesiones', 'Tiempo_en_Sitio', 'Productos_Visitados']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Modelo DBSCAN
dbscan = DBSCAN(eps=1.2, min_samples=6)
df['cluster'] = dbscan.fit_predict(X_scaled)

# Visualización (2 primeras dimensiones)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=df['cluster'], cmap='viridis')
plt.xlabel('Visitas (Normalizado)')
plt.ylabel('Sesiones (Normalizado)')
plt.title('DBSCAN en Comportamiento de Usuarios')
plt.show()
