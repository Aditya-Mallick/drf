from urllib import response
import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    "title": "This is data passed to CreateApiView",
    "price": 32.99
}
response = requests.post(endpoint, json=data)
print(response.json())
