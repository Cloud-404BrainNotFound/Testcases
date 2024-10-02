import requests

local = 1
if local:
    url = 'http://localhost:8001/users/login'
else:
    url = 'http://34.203.249.254:8001/users/login'

data = {
    "email": "123242155@example.com",
    "password": "password123"
}

response = requests.post(url, data=data)
print(response.text)