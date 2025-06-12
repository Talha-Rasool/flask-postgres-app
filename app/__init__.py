from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Register blueprint
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .health.check import health as health_blueprint
    app.register_blueprint(health_blueprint)

    return app


