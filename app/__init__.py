from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from app.task.controller import task_bp
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Create a parent blueprint and register it with its sub-blueprints with the Flask app
    parent_bp = Blueprint('parent', __name__, url_prefix='/api/v1')
    parent_bp.register_blueprint(task_bp, url_prefix='/tasks')
    app.register_blueprint(parent_bp)

    # Initialize Flask-SQLAlchemy
    db.init_app(app)

    return app
