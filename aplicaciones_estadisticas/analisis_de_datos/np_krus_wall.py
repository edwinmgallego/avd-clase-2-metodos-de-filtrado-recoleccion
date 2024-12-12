from scipy.stats import kruskal

# Simular tres grupos
grupo1 = np.random.rand(20)
grupo2 = np.random.rand(20) + 1
grupo3 = np.random.rand(20) + 2

stat, p = kruskal(grupo1, grupo2, grupo3)
print(f"Estadístico: {stat}, Valor p: {p}")
