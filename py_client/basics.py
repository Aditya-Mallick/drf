import requests

endpoint = "http://localhost:8000/api/"

response = requests.post(
    endpoint, json={"title": "This is hello ", "price": "Hello from basic"})
print(response.json())
print(response.status_code)
