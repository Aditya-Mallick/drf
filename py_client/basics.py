import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, params={'abc': 1}, json={
                        "query": "This is parameter json"})
print(response.json())
print(response.status_code)
