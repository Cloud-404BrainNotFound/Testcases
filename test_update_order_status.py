import requests

local = 1
if local:
    url = 'http://localhost:8004/orders/orders'
else:
    url = 'http://54.237.161.55:8004/orders/orders'

# Test updating order status
order_id = "254a696f-ce24-4d6c-a8dd-99ae712fd35a"  # Replace with a valid order ID from your data
data = {
    "order_status": "paid"  # Updating status to 'paid'
}

response = requests.put(f"{url}/{order_id}/status", json=data)

# Validate response
if response.status_code == 200:
    print("Test passed: Order status updated successfully.")
else:
    print("Test failed: Unexpected response status code", response.status_code)

# Print the response body
print(response.json())
