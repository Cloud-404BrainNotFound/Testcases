import requests

local = 0
if local:
    url = 'http://localhost:8001/users/login'
else:
    url = 'http://54.237.161.55:8001/users/login'

data = {
    "email": "123242155@example.com",
    "password": "password123"
}

response = requests.post(url, data=data)
print(response.text)