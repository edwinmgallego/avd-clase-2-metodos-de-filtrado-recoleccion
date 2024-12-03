import requests
from bs4 import BeautifulSoup

# Obtener el contenido de una página
url = 'https://datos.cali.gov.co/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extraer un título
titulo = soup.find('h2').text
print(titulo)
