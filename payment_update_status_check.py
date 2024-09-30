import requests

url = 'http://localhost:8000/payments/update_status'
local = 0
if local:
    url = 'http://localhost:8000/payments/update_status'
else:
    url = 'http://34.203.249.254:8002/payments/update_status'
data = {"payment_id": "00093d02-751f-4f34-a53c-b04c42fc5d33",  
        "status": "COMPLETED"}

response = requests.post(url, json=data)
print(response.text)