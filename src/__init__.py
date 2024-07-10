from logging import getLogger
from logging.config import fileConfig as logConfig

from flask import Flask
from flask_restx import Api

from src.config import Config
from src.controllers import register_namespaces

logConfig("./logging.conf", disable_existing_loggers=False)
logger = getLogger(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    api = Api(
      title='Petlove API',
      version='1.0',
      description='Petlove API Documentation',
      prefix='/api/ecommerce/v1',
    )

    api.init_app(app)

    register_namespaces(api)

    return app

