# test_async_update.py
import requests


local = 1
if local:
    url = 'http://localhost:8004/orders/order_async_update'
else:
    url = 'http://54.237.161.55:8004/orders/order_async_update'

# Test asynchronous update of an order
order_id = "ad0cf15f-149f-4c48-b82c-5a81e51355cc"  # Replace with a valid order ID from your data

data = {
    "order_id": order_id
}

# Sending the POST request to trigger background task
response = requests.post(url, params=data)

# Check for response status code 202 (Accepted)
if response.status_code == 202:
    print("Test passed: Asynchronous update triggered successfully.")
else:
    print(f"Test failed: Unexpected response status code {response.status_code}")
    print(response.json())  # Print the response for debugging
