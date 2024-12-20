import seaborn as sns
import pandas as pd

# Dataset (usaremos el dataset 'tips' de Seaborn como ejemplo)
df = sns.load_dataset('tips')

# Matriz de correlación (sólo variables numéricas)
correlation_matrix = df.corr()

# Visualización con un heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Matriz de Correlación")
plt.show()

# Identificar correlaciones fuertes (>0.7 o <-0.7)
strong_correlations = correlation_matrix[(correlation_matrix > 0.7) | (correlation_matrix < -0.7)]
print("Correlaciones fuertes:")
print(strong_correlations)
