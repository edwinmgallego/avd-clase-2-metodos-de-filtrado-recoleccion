import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Cargar datos desde un archivo CSV
# Asegúrate de tener el archivo 'rendimiento_estudiantes.csv' en tu directorio de trabajo.
df = pd.read_csv('C:/Users/cript/OneDrive/Documentos/tecnalia_analisis_de_datos/clase-1/avd-clase-2-metodos-de-filtrado-recoleccion/dataset/rendimiento_estudiantes.csv')

# Visualizar los primeros datos
print(df.head())

# Verificar si hay valores faltantes
print("\nValores faltantes por columna:")
print(df.isnull().sum())

# Agrupar datos por escuela para realizar ANOVA
escuela_a = df[df['Escuela'] == 'Escuela A']['Puntaje']
escuela_b = df[df['Escuela'] == 'Escuela B']['Puntaje']
escuela_c = df[df['Escuela'] == 'Escuela C']['Puntaje']

# ANOVA
stat, p = f_oneway(escuela_a, escuela_b, escuela_c)

# Resultados
print(f"\nEstadístico F: {stat:.2f}")
print(f"P-valor: {p:.4f}")

if p < 0.05:
    print("Rechazamos la hipótesis nula: hay diferencias significativas entre los promedios de las escuelas.")
else:
    print("No se puede rechazar la hipótesis nula: no hay diferencias significativas entre los promedios de las escuelas.")

# Visualización: Gráfico de cajas (Boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Escuela', y='Puntaje', data=df, palette="coolwarm")
plt.title('Distribución de Puntuaciones por Escuela', fontsize=14)
plt.xlabel('Escuela', fontsize=12)
plt.ylabel('Puntaje', fontsize=12)
plt.show()

# Visualización: Gráfico de barras con promedios
promedios = df.groupby('Escuela')['Puntaje'].mean().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(x='Escuela', y='Puntaje', data=promedios, palette="coolwarm", ci=None)
plt.title('Promedios de Puntuaciones por Escuela', fontsize=14)
plt.xlabel('Escuela', fontsize=12)
plt.ylabel('Puntaje Promedio', fontsize=12)
plt.axhline(y=df['Puntaje'].mean(), color='gray', linestyle='--', label='Promedio General')
plt.legend()
plt.show()
