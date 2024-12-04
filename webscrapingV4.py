from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin  # Para construir enlaces completos

# Configurar Selenium
driver = webdriver.Chrome()
driver.get('https://www.elpais.com.co/')

# Esperar a que el contenido cargue (si es necesario)
driver.implicitly_wait(10)

# Extraer el contenido HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Base URL para construir enlaces completos
base_url = 'https://www.elpais.com.co'

# Buscar datos específicos
titulos = soup.find_all('h2', class_='text-lg')  # Asegúrate de que esta clase sea correcta
datos = []

for titulo in titulos:
    # Extraer el título
    texto_titulo = titulo.text.strip()
    
    # Buscar enlace asociado al título
    enlace_relativo = titulo.find('a')['href'] if titulo.find('a') else None
    enlace = urljoin(base_url, enlace_relativo) if enlace_relativo else 'Sin enlace'
    
    # Añadir los datos a la lista (sin fecha en este caso)
    datos.append([texto_titulo, enlace])

# Guardar los datos en un archivo CSV
with open('noticias.csv', mode='w', encoding='utf-8', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    # Escribir el encabezado
    escritor.writerow(['Título', 'Enlace'])
    # Escribir los datos
    escritor.writerows(datos)

# Cerrar navegador
driver.quit()

print("Datos guardados en noticias.csv")
