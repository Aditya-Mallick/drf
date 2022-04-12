from urllib import response
import requests

endpoint = 'http://localhost:8000/api/products/list/'

response = requests.get(endpoint)
print(response.json())
