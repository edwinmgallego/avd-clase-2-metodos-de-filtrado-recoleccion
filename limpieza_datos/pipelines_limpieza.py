import pandas as pd

def limpiar_datos(df):
    # Eliminar duplicados
#Eliminar duplicados: df.drop_duplicates() elimina las filas duplicadas del DataFrame.
#Manejar valores nulos: df.fillna(0) reemplaza los valores nulos con 0.
#Estandarizar texto: Si la columna 'Nombre' existe, convierte todos los nombres a minúsculas con df['Nombre'].str.lower().
    
    df = df.drop_duplicates()
    
    # Manejar valores nulos
    df = df.fillna(0)
    
    # Estandarizar texto
    if 'Nombre' in df.columns:
        df['Nombre'] = df['Nombre'].str.lower()
    
    return df

# Crear datos Aquí estamos creando un diccionario data con dos listas: una para los nombres y otra para las edades. Luego, convertimos este diccionario en un DataFrame de pandas usando pd.DataFrame(data).



data = {'Nombre': ['ANA', 'Luis', 'ANA'], 'Edad': [25, None, 30]}
df = pd.DataFrame(data)

# Aplicar pipeline Llamamos a la función limpiar_datos pasando el DataFrame df como argumento. El resultado es un nuevo DataFrame df_limpio con los datos limpios.
df_limpio = limpiar_datos(df)
print(df_limpio)