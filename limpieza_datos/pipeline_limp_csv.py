import pandas as pd

def limpiar_datos(df):
    # Eliminar duplicados
    df = df.drop_duplicates()
    
    # Manejar valores nulos
    df = df.fillna(0)
    
    # Estandarizar texto
    if 'Nombre' in df.columns:
        df['Nombre'] = df['Nombre'].str.lower()
    
    return df

# Crear datos
data = {'Nombre': ['ANA', 'Luis', 'ANA'], 'Edad': [25, None, 30]}
df = pd.DataFrame(data)

# Aplicar pipeline
df_limpio = limpiar_datos(df)

# Exportar a un archivo Excel
df_limpio.to_excel('datos_limpios.xlsx', index=False)

print("El DataFrame limpio ha sido exportado a 'datos_limpios.xlsx'.")