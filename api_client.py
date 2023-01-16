import requests


response = requests.get('http://127.0.0.1:8000/api/users/')

print(response.json())

response = requests.options('http://127.0.0.1:8000/api/users/')

print(response.json())

data = {'name': 'new category', 'rating': 12}

requests.post('http://127.0.0.1:8000/api/users/', data)