from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Datos de ejemplo
np.random.seed(0)
X = np.random.rand(100, 3)  # Tres variables independientes
y = 3 * X[:, 0] + 2 * X[:, 1] + X[:, 2] + np.random.randn(100)  # Variable dependiente

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Ajustar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

# Evaluación
print("Coeficientes:", model.coef_)
print("Intercepto:", model.intercept_)
print("Error cuadrático medio:", mean_squared_error(y_test, y_pred))
