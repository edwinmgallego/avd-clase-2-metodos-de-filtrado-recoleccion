#Importar la librería pandas:

import pandas as pd

# Crear datos con valores nulos  Aquí se crea un diccionario data con dos claves: 'Nombre' y 'Edad'. Luego, se convierte este diccionario en un DataFrame llamado df. El DataFrame resultante tiene algunos valores nulos (None).
data = {'Nombre': ['Ana', 'Luis', None], 'Edad': [25, None, 30]}

print (data)
df = pd.DataFrame(data)

# Eliminar filas con valores nulos   Esta línea elimina cualquier fila que contenga valores nulos en el DataFrame df, creando un nuevo DataFrame df_sin_nulos sin esas filas.
df_sin_nulos = df.dropna()

# Rellenar valores nulos con un valor constante
df_relleno = df.fillna({'Nombre': 'Desconocido', 'Edad': df['Edad'].mean()})
print(df_relleno)
