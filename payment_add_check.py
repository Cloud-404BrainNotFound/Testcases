import requests

# 配置测试环境的URL
local = 1
if local:
    base_url = 'http://localhost:8000'
else:
    base_url = 'http://54.237.161.55:8001'

# POST请求的URL
create_url = f"{base_url}/payments/payments"

# 请求数据
data = {
    "card_number": "1234567812345678",
    "expiry_month": "12",
    "expiry_year": "25",
    "cvc": "123"
}

# 发送POST请求
response = requests.post(create_url, json=data)

# 输出响应结果
if response.status_code == 200:
    print("Test Passed: Payment created successfully.")
    print("Response:", response.json())
else:
    print("Test Failed: Unexpected status code.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)