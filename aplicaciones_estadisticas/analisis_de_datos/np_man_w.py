from scipy.stats import mannwhitneyu
import numpy as np

# Simulación de datos
grupo1 = np.random.rand(20) + 1
grupo2 = np.random.rand(20)

stat, p = mannwhitneyu(grupo1, grupo2)
print(f"Estadístico: {stat}, Valor p: {p}")
