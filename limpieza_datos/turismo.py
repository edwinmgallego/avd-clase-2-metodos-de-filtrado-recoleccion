import pandas as pd

# Cargar el archivo CSV
file_path = 'C:/Users/cript/OneDrive/Documentos/tecnalia_analisis de datos/clase-1/avd-clase-2-metodos-de-filtrado-recoleccion/dataset/dataset_turismo.csv'  # Cambia esto por la ruta de tu archivo
dataset = pd.read_csv(file_path)

# Reemplazar "N/A" y valores NaN por "desconocido"
dataset.replace("N/A", "desconocido", inplace=True)
dataset.fillna("desconocido", inplace=True)

# Reemplazar "desconocido" por "eco-turismo" si "Motivo Viaje" es "Cultural"
condition = (dataset["Motivo Viaje"] == "Cultural") & (dataset["Otro motivo de viaje o consulta PIT-Cual?"] == "desconocido")
dataset.loc[condition, "Otro motivo de viaje o consulta PIT-Cual?"] = "eco-turismo"

# Imprimir el dataset modificado
print("Dataset modificado:")
print(dataset)

# Guardar el archivo modificado
output_path = 'dataset_modificado.csv'  # Cambia esto por la ruta de salida deseada
dataset.to_csv(output_path, index=False)

print(f"\nEl archivo ha sido procesado y guardado en {output_path}")