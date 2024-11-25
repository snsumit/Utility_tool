from flask import Flask
from app.routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")
    app.config['UPLOAD_FOLDER'] = "instance/uploads"
    register_blueprints(app)
    return app

