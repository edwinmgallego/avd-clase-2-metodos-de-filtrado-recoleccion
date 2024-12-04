from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Configurar Selenium
driver = webdriver.Chrome()
driver.get('https://www.elpais.com.co/')

# Esperar a que el contenido cargue (si es necesario)
driver.implicitly_wait(10)

# Extraer el contenido HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Buscar datos específicos
titulos = soup.find_all('h2', class_='text-lg')
for titulo in titulos:
    print(titulo.text)

# Cerrar navegador
driver.quit()
