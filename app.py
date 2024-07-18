-- Index.html contains main login code within Css in it.

-- apple.png google.png and facebook.png are the assest files

--deploy site link :- https://login-assignment-guyal.netlify.app

Instruction for app.py file:-

1) Save the script to a file, e.g., app.py.
2) Install Flask if you haven't already using pip install flask.
3) Run the script using python app.py.
4) The API will be available at http://127.0.0.1:5000/. --> if this throughs error use thunderclient-

Thunder Client is a popular VS Code extension for testing REST APIs. Here's how you can use Thunder Client to test your Flask API:
-- Installation
-- Open Visual Studio Code.
-- Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
-- Search for "Thunder Client" and install the extension.
-- This implementation uses a JSON file (users.json) to store user data and provides the five REST API endpoints as described.

--> Testing the API
1) Open Thunder Client: Click on the Thunder Client icon in the Activity Bar.
2) Create a New Request: Click on "New Request".
3) Configure the Request:
   Example Request in Thunder Client
-- GET /users
   
   1)Open Thunder Client and click "New Request".
   2) Set the method to GET.
   3) Set the URL to http://127.0.0.1:5000/users.
   4)  Click "Send".

-- POST /users
1) Open Thunder Client and click "New Request".
2) Set the method to POST.
3) Set the URL to http://127.0.0.1:5000/users.
4) Go to the "Body" tab and select "JSON".
5) Enter the following JSON data: {
  "username": "testuser",
  "email": "test@example.com"
}
6) Click "Send".

-- GET /users/1
1) Open Thunder Client and click "New Request".
2) Set the method to GET.
3) Set the URL to http://127.0.0.1:5000/users/1 (replace 1 with the actual user ID).
4) Click "Send".

-- PATCH /users/1
1) Open Thunder Client and click "New Request".
2) Set the method to PATCH.
3) Set the URL to http://127.0.0.1:5000/users/1 (replace 1 with the actual user ID).
4) Go to the "Body" tab and select "JSON".
5) Enter the following JSON data: {
  "username": "updateduser",
  "email": "updated@example.com"
}
6) Click "Send".

-- DELETE /users/1
1) Open Thunder Client and click "New Request".
2) Set the method to DELETE.
3) Set the URL to http://127.0.0.1:5000/users/1 (replace 1 with the actual user ID).
4) Click "Send".
