import requests

# 配置测试环境的URL
local = 1
if local:
    base_url = 'http://localhost:8000'
else:
    base_url = 'http://54.237.161.55:8001'

# 测试用用户ID（需替换为实际存在的ID）
user_id = "09683a52-857b-4549-9798-7d7ca4eca5e6"  # 要删除的用户ID

# DELETE请求的URL
delete_url = f"{base_url}/users/{user_id}"

# 发送DELETE请求
response = requests.delete(delete_url)

# 输出响应结果
if response.status_code == 200:
    print("Test Passed: User deleted successfully.")
    print("Response:", response.json())
elif response.status_code == 404:
    print("Test Failed: User not found.")
    print("Response:", response.json())
else:
    print("Test Failed: Unexpected status code.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)