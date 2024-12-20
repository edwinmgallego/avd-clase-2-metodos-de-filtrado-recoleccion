import pandas as pd
from scipy.stats import spearmanr

# Datos
data = {
    "Horas de Estudio": [2, 4, 6, 8, 10],
    "Calificaciones": [50, 60, 70, 80, 90]
}
df = pd.DataFrame(data)

# Cálculo del coeficiente de Spearman
coef, p = spearmanr(df["Horas de Estudio"], df["Calificaciones"])
print(f"Coeficiente de Spearman: {coef}, p-valor: {p}")

# Interpretación
if p < 0.05:
    print("Existe una correlación significativa.")
else:
    print("No existe una correlación significativa.")
