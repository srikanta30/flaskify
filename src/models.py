from pydantic import BaseModel, EmailStr
from src import mongo
from bson import ObjectId

class TodoModel(BaseModel):
    title: str
    description: str
    created_at: str
    is_completed: bool = False

class Todo:
    @classmethod
    def save_to_db(cls, todo: TodoModel):
        mongo.db.todos.insert_one(todo.dict())

    @classmethod
    def find_all(cls):
        todos = list(mongo.db.todos.find())
        for todo in todos:
            todo['_id'] = str(todo['_id'])
        return todos

    @classmethod
    def find_by_id(cls, todo_id):
        try:
            todo_id = ObjectId(todo_id)
        except:
            return None
        todo = mongo.db.todos.find_one({'_id': todo_id})
        if todo:
            todo['_id'] = str(todo['_id'])
        return todo

    @classmethod
    def update_todo(cls, todo_id, new_data):
        mongo.db.todos.update_one({'_id': ObjectId(todo_id)}, {'$set': new_data})

    @classmethod
    def delete_todo(cls, todo_id):
        mongo.db.todos.delete_one({'_id': ObjectId(todo_id)})

class UserModel(BaseModel):
    email: EmailStr
    password: str

class User:
    @classmethod
    def save_to_db(cls, user: UserModel):
        mongo.db.users.insert_one(user.dict())

    @classmethod
    def find_by_id(cls, user_id):
        return mongo.db.users.find_one({'_id': ObjectId(user_id)})

    @classmethod
    def find_by_email(cls, email):
        return mongo.db.users.find_one({'email': email})
