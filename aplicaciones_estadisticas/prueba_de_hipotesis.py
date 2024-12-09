import numpy as np
from scipy.stats import ttest_ind

# Datos simulados
grupo_a = np.random.normal(70, 5, 30)  # Promedio 70, SD 5
grupo_b = np.random.normal(65, 5, 30)  # Promedio 65, SD 5

# Prueba t
stat, p = ttest_ind(grupo_a, grupo_b)
print(f"Estadístico t: {stat:.2f}, p-valor: {p:.4f}")

if p < 0.05:
    print("Rechazamos la hipótesis nula: las medias son diferentes.")
else:
    print("No se puede rechazar la hipótesis nula.")
