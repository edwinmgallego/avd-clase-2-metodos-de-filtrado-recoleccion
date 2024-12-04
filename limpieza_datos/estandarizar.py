#Función parse_date:

#Intenta convertir una fecha usando varios formatos ('%Y/%m/%d' y '%d-%m-%Y').
#Si la conversión falla para un formato, intenta con el siguiente.
#Si ninguno de los formatos funciona, devuelve NaT.
#aplicar la función:

#Usamos apply para aplicar la función parse_date a cada valor en la columna Fecha.
#Resultado esperado:
#Este enfoque debería manejar correctamente las fechas en diferentes formatos y evitar el problema de obtener NaT para fechas válidas.

import pandas as pd

# Crear datos
data = {'Fecha': ['2024/01/01', '01-02-2024'], 'Nombre': ['ANA', 'Luis']}
df = pd.DataFrame(data)

# Función para intentar convertir fechas en varios formatos
def parse_date(date_str):
    for fmt in ('%Y/%m/%d', '%d-%m-%Y'):
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            continue
    return pd.NaT

# Aplicar la función a la columna 'Fecha'
df['Fecha'] = df['Fecha'].apply(parse_date)

# Convertir texto a minúsculas
df['Nombre'] = df['Nombre'].str.lower()
print(df)