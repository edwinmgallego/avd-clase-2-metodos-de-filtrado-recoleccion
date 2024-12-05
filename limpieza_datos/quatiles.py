#El error que estás viendo, NameError: name 'pd' is not defined, ocurre porque no has importado la librería `pandas` con el alias `pd`. Para solucionar esto, necesitas agregar la línea de importación de `pandas` al inicio de tu código.

#Definición: El IQR es la diferencia entre el tercer cuartil (Q3) y el primer cuartil (Q1) de un conjunto de datos. Los cuartiles dividen los datos ordenados en cuatro partes iguales:

#Q1 (primer cuartil): El valor que separa el 25% inferior de los datos.
#Q2 (segundo cuartil o mediana): El valor que separa el 50% inferior de los datos.
#Q3 (tercer cuartil): El valor que separa el 75% inferior de los datos.
#La fórmula es: $$\text{IQR} = Q3 - Q1$$
#
#Cálculo:
#
#Ordena los datos de menor a mayor.
#Encuentra Q1, que es el valor en el punto 25% de los datos.
#Encuentra Q3, que es el valor en el punto 75% de los datos.
#Resta Q1 de Q3 para obtener el IQR.
#Uso: El IQR es útil para identificar la dispersión de los datos y detectar valores atípicos (outliers). Los valores que están por debajo de $$Q1 - 1.5 \times IQR$$ o por encima de $$Q3 + 1.5 \times IQR$$ se consideran outliers12.
#
#Ejemplo: Supongamos que tienes los siguientes datos: [1, 3, 6, 7, 11, 12, 13, 20, 24, 25, 27, 31, 32, 33, 35, 40].
#
#Q1 sería 11 (el valor en el 25%).
#Q3 sería 31 (el valor en el 75%).
#Entonces, el IQR sería $$31 - 11 = 20$$.
#El IQR es una medida robusta porque no se ve afectada por valores extremos, a diferencia del rango total. ¿Te gustaría saber más sobre cómo aplicar el IQR en tus análisis de datos?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Crear datos
data = {'Valores': [10, 12, 15, 1000, 2000, 4000, 2500]}
df = pd.DataFrame(data)

# Calcular rango intercuartil (IQR)
q1 = df['Valores'].quantile(0.25)
q3 = df['Valores'].quantile(0.75)
iqr = q3 - q1

# Filtrar outliers
df_filtrado = df[(df['Valores'] >= q1 - 1.5 * iqr) & (df['Valores'] <= q3 + 1.5 * iqr)]

# Graficar el dataset original con outliers
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.boxplot(df['Valores'])
plt.title('Dataset con Outliers')
plt.ylabel('Valores')

# Graficar el dataset corregido sin outliers
plt.subplot(1, 2, 2)
plt.boxplot(df_filtrado['Valores'])
plt.title('Dataset Corregido (Sin Outliers)')
plt.ylabel('Valores')

plt.tight_layout()
plt.show()