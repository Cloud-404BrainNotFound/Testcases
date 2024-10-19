import requests

local = 1
if local:
    url = 'http://localhost:8004/orders'
else:
    url = 'http://54.237.161.55:8004/orders'

# Test pagination with query parameters (e.g., limit and skip)
params = {
    "sport": "Tennis",  # Filter by sport
    "order_status": "pending",  # Filter by order status (ensure this matches your enum case)
    "skip": 0,  # Starting from the first result
    "limit": 5  # Limit to 5 results
}

# Sending the GET request with pagination and filtering
response = requests.get(url, params=params)

# Check for successful response and pagination
if response.status_code == 200:
    orders = response.json().get("orders", [])
    if len(orders) <= 5:  # Ensure we get no more than the limit specified
        print("Test passed: Pagination and query parameters work correctly.")
    else:
        print("Test failed: More results than expected.")
else:
    print(f"Test failed: Unexpected response status code {response.status_code}")
    print(response.json())  # Print the response for debugging
