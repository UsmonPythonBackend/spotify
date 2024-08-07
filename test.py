import requests

api_url = 'http://localhost:8000/swagger/'

data = requests.get(api_url).json()
print(data)

