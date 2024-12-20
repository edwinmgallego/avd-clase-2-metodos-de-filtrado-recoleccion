import scipy.stats as stats

# Datos de ejemplo
grupo1 = [70, 75, 80, 85, 90]
grupo2 = [60, 65, 70, 75, 80]
grupo3 = [50, 55, 60, 65, 70]

# Prueba de Kruskal-Wallis
stat, p = stats.kruskal(grupo1, grupo2, grupo3)
print(f'Estadístico de prueba: {stat}, p-valor: {p}')