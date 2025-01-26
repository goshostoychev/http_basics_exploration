# Simple Python script to experiment with API requests

# Import the requests library
import requests

# GET method
response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
print(response.status_code)
print(response.json())