import scipy.stats as stats

# Datos de ejemplo
clase1 = [85, 90, 78, 92, 88]
clase2 = [80, 85, 84, 90, 87]

# Prueba de Mann-Whitney U
stat, p = stats.mannwhitneyu(clase1, clase2)
print(f'Estadístico de prueba: {stat}, p-valor: {p}')