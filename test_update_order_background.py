import requests

local = 1
if local:
    url = 'http://localhost:8004/orders/order_async_update'
else:
    url = 'http://54.237.161.55:8004/orders/order_async_update'

# Test asynchronous update of an order
order_id = "254a696f-ce24-4d6c-a8dd-99ae712fd35a"  # Replace with a valid order ID from your data
# data = {
#     "order_id": order_id
# }

# Sending the POST request to trigger background task
response = requests.post(f"{url}/{order_id}")

# Check for response status code 202 (Accepted)
if response.status_code == 202:
    print("Test passed: Asynchronous update triggered successfully.")
else:
    print("Test failed: Unexpected response status code", response.status_code)

# Print the response body
print(response.json())
