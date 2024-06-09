import os
import logging
from datetime import timedelta

from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, Api
from bson import ObjectId

from src import mongo, jwt
from src.models import Todo, User, UserModel, TodoModel
from src.validation import validate_request

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

logging.basicConfig(filename='access.log', level=logging.INFO)

class TodoListResource(Resource):
    @jwt_required()
    def get(self):
        try:
            todos = Todo.find_all()
            return todos, 200
        except Exception as e:
            logging.error(f"Error getting todos: {str(e)}")
            return {"message": "Internal Server Error"}, 500

    @jwt_required()
    @validate_request(TodoModel)
    def post(self):
        try:
            data = request.json
            Todo.save_to_db(TodoModel(**data))
            return {"message": "Todo created successfully"}, 201
        except Exception as e:
            logging.error(f"Error creating todo: {str(e)}")
            return {"message": "Internal Server Error"}, 500

class TodoResource(Resource):
    @jwt_required()
    def get(self, todo_id):
        try:
            todo = Todo.find_by_id(todo_id)
            if todo:
                return todo, 200
            return {"message": "Todo not found"}, 404
        except Exception as e:
            logging.error(f"Error getting todo: {str(e)}")
            return {"message": "Internal Server Error"}, 500

    @jwt_required()
    @validate_request(TodoModel)
    def put(self, todo_id):
        try:
            data = request.json
            Todo.update_todo(todo_id, data)
            return {"message": "Todo updated successfully"}, 200
        except Exception as e:
            logging.error(f"Error updating todo: {str(e)}")
            return {"message": "Internal Server Error"}, 500

    @jwt_required()
    def delete(self, todo_id):
        try:
            Todo.delete_todo(todo_id)
            return {"message": "Todo deleted successfully"}, 200
        except Exception as e:
            logging.error(f"Error deleting todo: {str(e)}")
            return {"message": "Internal Server Error"}, 500

class UserResource(Resource):
    @validate_request(UserModel)
    def post(self):
        try:
            data = request.json
            email = data.get('email')
            password = data.get('password')
            hashed_password = generate_password_hash(password)
            if User.find_by_email(email):
                return {"message": "User already exists"}, 400
            User.save_to_db(UserModel(email=email, password=hashed_password))
            return {"message": "User created successfully"}, 201
        except Exception as e:
            logging.error(f"Error creating user: {str(e)}")
            return {"message": "Internal Server Error"}, 500

class UserLoginResource(Resource):
    @validate_request(UserModel)
    def post(self):
        try:
            data = request.json
            email = data.get('email')
            password = data.get('password')
            user = User.find_by_email(email)
            if user and check_password_hash(user['password'], password):
                access_token = create_access_token(identity=str(user['_id']), expires_delta=timedelta(days=1))
                return {"access_token": access_token}, 200
            return {"message": "Invalid credentials"}, 401
        except Exception as e:
            logging.error(f"Error logging in: {str(e)}")
            return {"message": "Internal Server Error"}, 500

api.add_resource(TodoListResource, '/todos')
api.add_resource(TodoResource, '/todos/<string:todo_id>')
api.add_resource(UserResource, '/register')
api.add_resource(UserLoginResource, '/login')
