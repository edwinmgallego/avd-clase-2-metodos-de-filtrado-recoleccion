from scipy.stats import spearmanr

# Calcular Spearman
spearman_corr, _ = spearmanr(x, y)
print(f"Coeficiente de correlación de Spearman: {spearman_corr}")
