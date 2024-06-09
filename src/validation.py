from pydantic import ValidationError
from flask import jsonify, request

def validate_request(model):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                data = request.json
                model(**data)
            except ValidationError as e:
                return {'message': 'Validation error', 'errors': e.errors()}, 400
            return func(*args, **kwargs)
        return wrapper
    return decorator