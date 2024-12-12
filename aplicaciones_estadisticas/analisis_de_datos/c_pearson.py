from scipy.stats import pearsonr

# Generar datos
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

# Calcular correlación
corr, _ = pearsonr(x, y)
print(f"Coeficiente de correlación de Pearson: {corr}")
