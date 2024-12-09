#pandas es una librería para manipular datos en Python. Aquí se utiliza para crear y trabajar con un DataFrame, que es una estructura tabular (como una hoja de cálculo).





import pandas as pd

# Crear un DataFrame con alturas en diferentes unidades (incluyendo errores)
# Creamos un diccionario data con dos claves:
#'Nombre': Lista de nombres de personas.
#'Altura': Lista de alturas con diferentes unidades (pies, m, cm, in, mm).
#Usamos pd.DataFrame(data) para convertir el diccionario en un DataFrame.
data = {
    'Nombre': ['Ana', 'Luis', 'María', 'Juan', 'Pedro', 'Lucía'],
    'Altura': ['5.9 pies', '1.75 m', '180 cm', '6 pies', '70 in', '1800 mm']
}
df = pd.DataFrame(data)

print("Datos originales:")
print(df) # Mostrar los datos originales

# Función para convertir todas las alturas a centímetros
# altura.split()[0]:
#Divide el texto de la altura en palabras separadas por espacios.
#Extrae el número (primer elemento).
#Convierte el número a tipo float.

def convertir_a_cm(altura):
    try:
        if 'pies' in altura:  # Caso: Altura en pies
            valor = float(altura.split()[0])  # Extraer el número
            return valor * 30.48  # Conversión de pies a cm
        elif 'm' in altura and 'mm' not in altura:  # Caso: Altura en metros
            valor = float(altura.split()[0])
            return valor * 100  # Conversión de metros a cm
        elif 'cm' in altura:  # Caso: Altura ya en cm
            return float(altura.split()[0])
        elif 'mm' in altura:  # Caso: Altura en milímetros
            valor = float(altura.split()[0])
            return valor / 10  # Conversión de mm a cm
        elif 'in' in altura:  # Caso: Altura en pulgadas
            valor = float(altura.split()[0])
            return valor * 2.54  # Conversión de pulgadas a cm
        else:
            return "Error: Formato desconocido"  # Formato no reconocido
    except Exception as e:
        return f"Error: {e}"  # Manejo de errores generales

# Aplicar la función al DataFrame
#Usamos el método .apply(función) para aplicar la función convertir_a_cm a cada valor de la columna 'Altura'.
#Los resultados se almacenan en una nueva columna llamada 'Altura (cm)'.
df['Altura (cm)'] = df['Altura'].apply(convertir_a_cm)


#Esto imprime el DataFrame con la nueva columna 'Altura (cm)'. Ejemplo de salida
print("\nDatos con alturas convertidas a cm:")
print(df)
