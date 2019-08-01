from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from FormStorage.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from FormStorage.forms.routes import forms
    from FormStorage.errors.handlers import errors
    app.register_blueprint(forms)
    app.register_blueprint(errors)
    
    return app