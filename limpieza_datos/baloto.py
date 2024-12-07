import requests
from bs4 import BeautifulSoup
from collections import Counter

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
    
    # Extraer las filas de la tabla
    rows = table.find_all("tr")[1:]  # Ignorar el encabezado
    
    # Extraer los datos de las columnas "Números Baloto" y "Números Revancha"
    baloto_numbers = []
    revancha_numbers = []
    for row in rows:
        cols = row.find_all("td")
        baloto_numbers.extend(cols[2].text.strip().split(", "))  # Columna "Números Baloto"
        revancha_numbers.extend(cols[3].text.strip().split(", "))  # Columna "Números Revancha"
    
    # Contar la frecuencia de cada número en "Números Baloto"
    baloto_count = Counter(baloto_numbers)
    least_common_baloto = baloto_count.most_common()[:-7:-1]  # Los 6 números menos comunes
    
    # Contar la frecuencia de cada número en "Números Revancha"
    revancha_count = Counter(revancha_numbers)
    least_common_revancha = revancha_count.most_common()[:-7:-1]  # Los 6 números menos comunes
    
    # Mostrar los resultados
    print("Los 6 números que menos se repiten en 'Números Baloto' son:")
    for num, freq in least_common_baloto:
        print(f"Número {num}: {freq} veces")
    
    print("\nLos 6 números que menos se repiten en 'Números Revancha' son:")
    for num, freq in least_common_revancha:
        print(f"Número {num}: {freq} veces")
else:
    print(f"Error al acceder a la página: {response.status_code}")