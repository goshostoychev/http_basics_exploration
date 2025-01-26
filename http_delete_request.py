# Simple Python script to experiment with APIs requests

# Import the requests library
import requests

# DELETE method
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())