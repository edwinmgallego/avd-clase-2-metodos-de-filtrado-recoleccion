from scipy.stats import chi2_contingency

# Datos categóricos simulados
tabla = [[10, 20, 30], [6, 15, 25]]
chi2, p, dof, expected = chi2_contingency(tabla)

print(f"Estadístico Chi-cuadrado: {chi2}")
print(f"Valor p: {p}")
print(f"Grados de libertad: {dof}")
