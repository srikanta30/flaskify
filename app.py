from flask import Flask
from config import app_config
from src import init_app
from src.views import api_bp
from flask_swagger_ui import get_swaggerui_blueprint

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    init_app(app)

    app.register_blueprint(api_bp, url_prefix='/api')

    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={  
            'flaskify': "API Documentation"
        }
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app

if __name__ == "__main__":
    app = create_app("development")
    app.run(host='0.0.0.0', port=8000)