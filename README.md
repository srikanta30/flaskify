Flask and MongoDB Task

Overview:
Your task is to build a web application using Flask as the backend framework and MongoDB as the database. The application should allow users to manage a collection of ToDos, and you are required to implement JWT token validation using middleware.

Requirements:

Setup:
● Initialize a new Flask project.
● Configure the project to connect to a MongoDB database.
● Implement user authentication using JWT (JSON Web Tokens).

Data Model:
● Define a MongoDB schema for an item with attributes such as id, name,
description, and created_at. API Endpoints:
● Implement RESTful API endpoints for the following operations:
● Create a new item
● Retrieve a list of all items
● Retrieve a specific item by ID
● Update an existing item
● Delete an item

Middleware - JWT Token Validation:
● Implement a middleware function to check the validity of the JWT token for
secured routes.
● Apply the middleware to the API endpoints, ensuring that only authenticated
users can perform CRUD operations. Validation:
● Enhance input validation to ensure the correctness and security of data.
● Validate the JWT token payload for necessary information. Documentation:
● Provide clear documentation on how to run the application locally, authenticate using JWT, and interact with the API endpoints.

Evaluation Criteria:
● Code Quality:
● Clean and well-organized code.
● Adherence to Python and Flask coding standards.
● Database Interaction:
● Proper integration with MongoDB.
● Effective use of MongoDB queries.
● API Design:
● RESTful design principles.
● Proper error handling.

● Middleware Implementation:
● Correct implementation of JWT token validation middleware.
● Secure handling of authenticated routes.
● Validation:
● Effective input and token payload validation.

Submission:
● Create a new repository for your work.
● Commit your code regularly with meaningful commit messages.
● Provide a comprehensive README.md file with instructions on setting up, running
the application, JWT authentication, and interacting with the API.