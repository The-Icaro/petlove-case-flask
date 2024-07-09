from logging import getLogger
from logging.config import fileConfig as logConfig

from flask import Flask
from flask_restx import Api

from src.controllers import register_namespaces

logConfig("./logging.conf", disable_existing_loggers=False)
logger = getLogger(__name__)

def create_app():
    app = Flask(__name__)

    api = Api(
      title='Petlove API',
      version='1.0',
      description='Petlove API Documentation',
    )

    api.init_app(app)

    register_namespaces(api)

    return app

