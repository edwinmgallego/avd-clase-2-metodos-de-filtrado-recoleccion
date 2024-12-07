import requests
import matplotlib.pyplot as plt
import pandas as pd

# Configuración de la API
API_KEY = 'L5CKN5DNL2RT0ZO0'
BASE_URL = 'https://www.alphavantage.co/query'

# Parámetros para la solicitud
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'IBM',
    'apikey': API_KEY
}

# Hacer la solicitud
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    print('Respuesta exitosa')
else:
    print('Error en la respuesta')
    exit()

# Procesar los datos de la respuesta
data = response.json()

# Validar que se obtuvieron datos correctamente
if "Time Series (Daily)" not in data:
    print("No se encontraron datos válidos.")
    exit()

# Obtener los precios diarios
daily_data = data["Time Series (Daily)"]

# Crear un DataFrame con los datos
df = pd.DataFrame.from_dict(daily_data, orient="index")  # Las fechas serán índices
df.index = pd.to_datetime(df.index)  # Convertir el índice a formato de fecha
df.sort_index(inplace=True)  # Ordenar por fecha

# Seleccionar solo los precios de cierre
df["4. close"] = df["4. close"].astype(float)  # Convertir a tipo numérico

# Agrupar por mes y calcular el promedio de cierre
monthly_data = df["4. close"].resample("M").mean()  # Resample por mes y calcular promedio

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data.values, label="Promedio mensual de cierre (USD)", color='orange', marker='o')

# Configurar el gráfico
plt.title("Precio promedio mensual de cierre de IBM", fontsize=16)
plt.xlabel("Fecha", fontsize=12)
plt.ylabel("Precio promedio (USD)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
