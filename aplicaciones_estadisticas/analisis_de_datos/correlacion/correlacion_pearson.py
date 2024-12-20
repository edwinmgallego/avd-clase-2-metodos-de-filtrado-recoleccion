import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Datos simulados
np.random.seed(42)
ingresos = np.random.normal(5000, 1000, 100)
gastos = ingresos * 0.5 + np.random.normal(0, 200, 100)

# Cálculo del coeficiente de Pearson
coef, p = pearsonr(ingresos, gastos)
print(f"Coeficiente de Pearson: {coef}, p-valor: {p}")

# Visualización
plt.scatter(ingresos, gastos, alpha=0.7, color='blue')
plt.title("Relación entre Ingresos y Gastos")
plt.xlabel("Ingresos")
plt.ylabel("Gastos")
plt.show()
