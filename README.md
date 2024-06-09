# Flaskify

This is a Flask application designed to manage Todos and user authentication.

## Instructions to Run

To run this Flask application, you can follow these steps:

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/srikanta30/flaskify.git
```

### 2. Install Docker

Ensure you have Docker installed on your machine. You can download and install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).

### 3. Build Docker Image

Navigate to the project directory and build the Docker image using the provided Dockerfile:

```bash
cd your-repository
docker build -t flaskify .
```

### 4. Run Docker Container

Once the Docker image is built, you can run the Docker container:

```bash
docker run -d -p 8000:8000 --name flaskify flaskify
```

### 5. Access the Application

You can now access the Flask application at `http://localhost:8000`.

## Routes

- `GET /todos`: Retrieve all todos.
- `POST /todos`: Create a new todo.
- `GET /todos/<todo_id>`: Retrieve a specific todo by ID.
- `PUT /todos/<todo_id>`: Update a specific todo by ID.
- `DELETE /todos/<todo_id>`: Delete a specific todo by ID.
- `POST /register`: Register a new user.
- `POST /login`: Login with user credentials.

### Swagger Documentation

After running the Flask application, you can access the Swagger documentation by navigating to the following URL in your web browser:

```
http://localhost:8000/api/docs/
```

This URL will open up the Swagger UI, allowing you to interactively explore and test the API endpoints. Swagger provides a user-friendly interface for understanding the API's functionality and testing different requests.

Feel free to explore the various endpoints and experiment with different requests using the Swagger documentation.

## Environment Variables

The following environment variables can be configured:

- `FLASK_ENV`: Set to `"development"` for development environment.
- `PORT`: Port on which the application will run. Default is `8000`.

## Additional Notes

- This application uses MongoDB for data storage. Ensure you have MongoDB installed and running.
- You may need to update `.env` file with appropriate configurations, see the `.env.example` file to see how the .env file should be.