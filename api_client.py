import requests
import base64


URL = 'http://127.0.0.1:8000/drf-api/'

# неавторизованный пользователь
response = requests.get(URL)
print(response.status_code)
print(response.json())

# Base Auth
response = requests.get(URL, auth=('auth', 'auth123456'))
print(response.status_code)
print(response.json())

# Base Auth
response = requests.get(URL, auth=('staff', 'staff123456'))
print(response.status_code)
print(response.json())

login = 'staff'
password = 'staff123456'
pair = f'{login}:{password}'
# auth_header = 'Basic c3RhZmY6c3RhZmYxMjM0NTY='
auth_header = f'Basic {base64.b64encode(pair.encode()).decode()}'
print(auth_header)
headers = {
    #'Authorization': f'Basic {base64.b64encode(pair.encode())}'
    'Authorization': auth_header
}
# Base Auth
response = requests.get(URL, headers=headers)
print(response.status_code)
print(response.json())
#
# TOKEN = 'f0d7cbebc19aaf098f52ec5a4d877c16e0ddf62a'
#
# headers = {
#     'Authorization': f'Token {TOKEN}'
# }
# #
# response = requests.get(URL, headers=headers)
# print(response.status_code)
# print(response.json())

header_code = b'c3RhZmY6c3RhZmYxMjM0NTY'

# print(base64.b64decode(header_code))

print('*'*100)
URL = 'http://127.0.0.1:8000/user/'

headers = {
    'Accept': 'application/json; version=v2.0'
}

response = requests.get(URL, headers=headers)
print(response.json())
