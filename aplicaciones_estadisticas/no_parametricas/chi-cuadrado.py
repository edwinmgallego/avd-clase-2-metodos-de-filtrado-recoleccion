import pandas as pd
import scipy.stats as stats

# Datos de ejemplo
data = {'Genero': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
        'Preferencia': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'B']}
df = pd.DataFrame(data)

# Tabla de contingencia
contingencia = pd.crosstab(df['Genero'], df['Preferencia'])

# Prueba de Chi-cuadrado
stat, p, dof, expected = stats.chi2_contingency(contingencia)
print(f'Estadístico de prueba: {stat}, p-valor: {p}')