import pandas as pd

# Crear datos con duplicados Aquí, estamos creando un diccionario llamado data que contiene dos listas: una para los IDs y otra para los valores. Observa que el ID 2 y el valor 200 están duplicados.
data = {'ID': [1, 2, 2], 'Valor': [100, 200, 200]}
df = pd.DataFrame(data)

# Eliminar duplicados Aquí, usamos el método drop_duplicates() de pandas para eliminar las filas duplicadas del DataFrame df. El DataFrame resultante, sin duplicados, se almacena en la variable df_sin_duplicados.
df_sin_duplicados = df.drop_duplicates()
print(df_sin_duplicados)