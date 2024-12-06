import requests

# Tu clave API de Alpha Vantage
API_KEY = "IU5GZ9EZGGM4BQDT"

# URL base de la API
BASE_URL = "https://www.alphavantage.co/query"

# Parámetros para obtener datos de la acción
params = {
    "function": "TIME_SERIES_DAILY",  # Tipo de datos (ej. diario)
    "symbol": "AAPL",                # Símbolo de la acción (ej. Apple)
    "apikey": API_KEY                # Tu clave API
}

# Realizar la solicitud
response = requests.get(BASE_URL, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()  # Convertir la respuesta a formato JSON
    print(data)             # Imprimir los datos
    
else:
    print("Error al obtener datos:", response.status_code)