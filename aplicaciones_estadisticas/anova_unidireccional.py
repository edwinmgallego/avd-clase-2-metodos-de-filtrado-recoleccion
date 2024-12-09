#Práctico Mejorado: ANOVA Unidireccional
#Contexto:
#Queremos analizar si hay diferencias significativas en los tiempos de reacción de tres grupos de personas sometidas a diferentes estímulos visuales (Grupo A, Grupo B y Grupo C).

#Código Mejorado con Visualizaciones:
#Incluiremos:

#Gráficos de cajas para comparar los datos.
#Visualización de los valores promedio.
#Resultado e interpretación del ANOVA.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Generar datos simulados
np.random.seed(42)
grupo1 = np.random.normal(10, 2, 30)  # Grupo A
grupo2 = np.random.normal(12, 2, 30)  # Grupo B
grupo3 = np.random.normal(14, 2, 30)  # Grupo C

# Crear DataFrame para graficar
data = pd.DataFrame({
    'Grupo': ['A']*30 + ['B']*30 + ['C']*30,
    'Tiempo de Reacción': np.concatenate([grupo1, grupo2, grupo3])
})

# Visualización: Gráfico de cajas (boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Grupo', y='Tiempo de Reacción', data=data, palette="coolwarm")
plt.title('Distribución de Tiempos de Reacción por Grupo', fontsize=14)
plt.xlabel('Grupo', fontsize=12)
plt.ylabel('Tiempo de Reacción', fontsize=12)
plt.show()

# ANOVA
stat, p = f_oneway(grupo1, grupo2, grupo3)

# Mostrar resultados
print(f"Estadístico F: {stat:.2f}")
print(f"P-valor: {p:.4f}")

if p < 0.05:
    print("Rechazamos la hipótesis nula: hay diferencias significativas entre los grupos.")
else:
    print("No se puede rechazar la hipótesis nula: no hay diferencias significativas entre los grupos.")

# Visualización: Promedios por grupo
promedios = data.groupby('Grupo')['Tiempo de Reacción'].mean().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(x='Grupo', y='Tiempo de Reacción', data=promedios, palette="coolwarm", ci=None)
plt.title('Promedios de Tiempos de Reacción por Grupo', fontsize=14)
plt.xlabel('Grupo', fontsize=12)
plt.ylabel('Tiempo de Reacción Promedio', fontsize=12)
plt.axhline(y=data['Tiempo de Reacción'].mean(), color='gray', linestyle='--', label='Promedio General')
plt.legend()
plt.show()
