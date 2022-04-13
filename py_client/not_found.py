import requests

endpoint = 'http://localhost:8000/api/products/13453455/'

response = requests.get(endpoint)
print(response.json())
