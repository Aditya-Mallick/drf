import requests

endpoint = 'http://localhost:8000/api/products/6/'

response = requests.get(endpoint)
print(response.json())
