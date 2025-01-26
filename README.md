# HTTP basics exploration
A simple Python project that interacts with an existing public API to demonstrate key HTTP concepts.

Bellow is a short summary, describing HTTP methods used during the tests I conducted, in relation to the “HTTP Basics” lecture from the Programming Fundamentals with Python Module by SoftUni.

HTTP methods used in the test and their purposes

The following HTTP methods were used during the tests:
1.	GET - The GET method is used to retrieve data on a server. Clients can use the GET method to access all of the resources of a given type, or they can use it to access a specific resource. For example, the GET request to the API  https://jsonplaceholder.typicode.com/posts/1/comments" returns some random generated posts, along with their ID, the user, email and the body of the post. Here’s how the GET request looks like in Postman:

![image](https://github.com/user-attachments/assets/f76d4f59-f09b-49fc-9cf6-008a68db5ad4)

 
The status code is 200 OK and indicates that the request has succeeded.

2.	POST - The POST method is used to create new resources. Unlike GET requests, POST requests typically include a request body, which is where the client specifies the attributes of the resource to be created. A POST request to the /posts endpoint of JSONPlaceholder might have a request body that looks like this:
   
```
   {
       "userId": 1,
       "id": 101,
       "title": "Testing POST method",
       "body": "Testing the POST method to JSONPlaceholder with Postman."
   }
```

Here’s how the POST request looks like in Postman:

![image](https://github.com/user-attachments/assets/48117486-4f42-4108-bd4f-41931f8c0cbb)

 
The status code is 201 Created, and indicates that the request has succeeded and has led to the creation of a resource. 

PUT - The PUT method is used to replace an existing resource with an updated version. This method works by replacing the entire resource (i.e., the specific product located at the /posts/1 endpoint) with the data that is included in the request’s body. This means that any fields or properties not included in the request body are deleted, and any new fields or properties are added. A PUT request to the /posts/1 endpoint of JSONPlaceholder might have a request body that looks like this:

    {
        "userId": 123,
        "newtitle": "Testing PUT method with additional field",
        "newbody": "Testing the PUT method to JSONPlaceholder with Postman and changin the body field."
    }


Here’s how the PUT request looks like in Postman:

![image](https://github.com/user-attachments/assets/c55a404d-d689-460e-8f99-5b094af96e8d)

 
Again, the status code is 200 OK and indicates that the request has succeeded.

9.	DELETE - The DELETE method is used to remove data from a database. When a client sends a DELETE request, it is requesting that the resource at the specified URL be removed. For example, a DELETE request to the / posts/1 endpoint will permanently remove the post with an ID of 1 from the database.

Here’s how the POST request looks like in Postman:

![image](https://github.com/user-attachments/assets/b113a7c0-66ef-4041-bd70-c24ad9a6ad44)

 
The status code is 200 OK and indicates that the request has succeeded and the resource has been deleted.

In the response headers of each method, we can see different values for the Content-Length, Vary, X-Content-Type-Options, Etag, etc.
