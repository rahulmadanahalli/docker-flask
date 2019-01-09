# app/__init__.py

from flask import Flask

# local import
from config import app_config
from main import app_bp


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(app_bp)
    
    is_prod = True if config_name == "production" else False
    
    # initialize pickledb
    print("Loading " + config_name + " app...")
    app.config_name = config_name

    return app

