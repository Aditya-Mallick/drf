import requests

endpoint = 'http://localhost:8000/api/products/1/update/'

response = requests.put(endpoint, json={'title': 'Hello world', 'price': 0.0})
print(response.json())
