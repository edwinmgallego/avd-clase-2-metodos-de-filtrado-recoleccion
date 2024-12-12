import statsmodels.api as sm

# Simular datos
np.random.seed(42)
x = np.random.rand(100)
y = 3 * x + np.random.normal(0, 0.5, 100)

# Modelo de regresión
X = sm.add_constant(x)  # Agregar constante para intercepto
modelo = sm.OLS(y, X).fit()

print(modelo.summary())
