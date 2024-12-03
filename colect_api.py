import requests

# Consumir una API
response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
