import requests

url = 'http://localhost:8001/users/signup'
local = 0
if local:
    url = 'http://localhost:8001/users/signup'
else:
    url = 'http://54.237.161.55:8001/users/signup'
data = {
    "username": "tes2t_user",
    "email": "123242155@example.com",
    "password": "password123",
    "role": "CUSTOMER",  # CUSTOMER or MERCHANT
    "store_id": "store123"  # 可选
}

response = requests.post(url, json=data)
print(response.text)