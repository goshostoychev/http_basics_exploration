# Simple Python script to experiment with API requests

# Import the requests library
import requests

# PUT method
response = requests.put("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())