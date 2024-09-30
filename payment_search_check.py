import requests

url = 'http://localhost:8000/payments/search'
local = 0
if local:
    url = 'http://localhost:8000/payments/search'
else:
    url = 'http://34.203.249.254:8002/payments/search'
data = {"user_id": "123456"}
response = requests.post(url, json=data)
print(response.text)