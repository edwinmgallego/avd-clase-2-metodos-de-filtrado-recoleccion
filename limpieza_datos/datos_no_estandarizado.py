import pandas as pd
import numpy as np

# Cargar datos de ejemplo
data = {
    'Name': [' Alice ', 'BOB', 'alice', 'Bob ', 'CHARLIE '],
    'Date': ['2023-01-01', '01/02/2023', '03-01-2023', np.nan, '2023/04/01'],
    'Price': ['100$', '200 ', None, '300.50$', '400USD']
}
df = pd.DataFrame(data)

print("Datos originales:")
print(df)

# **1. Limpieza de texto: Espacios y formatos consistentes**
# Quitar espacios y poner en formato título (Title Case)
df['Name'] = df['Name'].str.strip().str.title()

# **2. Limpieza de fechas: Estandarizar formato**
# Convertir todas las fechas al mismo formato
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Maneja fechas no válidas como NaT

# **3. Limpieza de precios: Eliminar caracteres no numéricos**
df['Price'] = df['Price'].str.replace(r'[^\d.]', '', regex=True).astype(float)

# **4. Manejo de valores nulos**
# Rellenar fechas faltantes con un valor predeterminado
df['Date'] = df['Date'].fillna('2023-01-01')

# Rellenar precios faltantes con la media
df['Price'] = df['Price'].fillna(df['Price'].mean())

# **5. Eliminar duplicados**
df.drop_duplicates(subset=['Name'], inplace=True)

print("\nDatos limpios:")
print(df)