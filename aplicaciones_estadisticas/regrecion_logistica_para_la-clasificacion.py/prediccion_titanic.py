import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

# Cargar dataset Titanic
titanic = sns.load_dataset('titanic')

# Preprocesamiento
titanic = titanic[['survived', 'pclass', 'sex', 'age', 'fare']].dropna()
titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})
X = titanic[['pclass', 'sex', 'age', 'fare']]
y = titanic['survived']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelo
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluación
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]
print("Reporte de Clasificación:\n", classification_report(y_test, y_pred))
print("AUC-ROC:", roc_auc_score(y_test, y_pred_proba))
