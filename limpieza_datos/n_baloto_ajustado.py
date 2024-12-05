import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL del sitio web
url = "https://www.balotoresultados.co/historico"

# Hacer la solicitud HTTP
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Buscar la tabla que contiene los datos
    table = soup.find("table")
    
    # Extraer los encabezados de la tabla
    headers = [header.text.strip() for header in table.find_all("th")]
    
    # Extraer las filas de la tabla
    rows = table.find_all("tr")[1:]  # Ignorar el encabezado
    
    # Extraer los datos de cada fila
    data = []
    for row in rows:
        cols = row.find_all("td")
        row_data = [col.text.strip().replace("\n", ", ") for col in cols]  # Reemplazar "\n" por ", "
        data.append(row_data)
    
    # Crear un DataFrame con los datos
    df = pd.DataFrame(data, columns=headers)
    
    # Mostrar los primeros registros del DataFrame
    print(df.head())
    
    # Guardar los datos en un archivo CSV
    df.to_csv("baloto_historico.csv", index=False)
    print("Datos guardados en 'baloto_historico.csv'")
else:
    print(f"Error al acceder a la página: {response.status_code}")