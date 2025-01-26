# Simple Python script to experiment with API requests

# Import the requests library
import requests

# POST method
response = requests.post("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
print(response.json())