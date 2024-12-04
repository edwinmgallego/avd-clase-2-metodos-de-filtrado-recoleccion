from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# Configurar Selenium
driver = webdriver.Chrome()
driver.get('https://www.elpais.com.co/')

# Esperar a que el contenido cargue (si es necesario)
driver.implicitly_wait(10)

# Extraer el contenido HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Buscar datos específicos
titulos = soup.find_all('h2', class_='text-lg')  # Asegúrate de que esta clase sea correcta
datos = []

for titulo in titulos:
    # Extraer el título
    texto_titulo = titulo.text.strip()
    
    # Buscar enlace asociado al título
    enlace = titulo.find('a')['href'] if titulo.find('a') else 'Sin enlace'
    
    # Buscar fecha si existe (reemplaza 'class_de_fecha' por la clase real si aplica)
    fecha = titulo.find_next('time').text.strip() if titulo.find_next('time') else 'Sin fecha'
    
    # Añadir los datos a la lista
    datos.append([texto_titulo, enlace, fecha])

# Guardar los datos en un archivo CSV
with open('noticias.csv', mode='w', encoding='utf-8', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    # Escribir el encabezado
    escritor.writerow(['Título', 'Enlace', 'Fecha'])
    # Escribir los datos
    escritor.writerows(datos)

# Cerrar navegador
driver.quit()

print("Datos guardados en noticias.csv")
