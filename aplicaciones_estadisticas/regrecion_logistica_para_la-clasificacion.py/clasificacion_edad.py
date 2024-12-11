import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Crear datos
np.random.seed(42)
ages = np.random.randint(10, 50, size=100)
is_adult = (ages >= 18).astype(int)
df = pd.DataFrame({'age': ages, 'is_adult': is_adult})

# Modelo
X = df[['age']]
y = df['is_adult']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
print("Precisión:", model.score(X_test, y_test))
