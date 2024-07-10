from flask_restx import Api

from src.controllers.health_controller import health_namespace
from src.controllers.question_controller import question_namespace


def register_namespaces(api: Api):
    api.add_namespace(health_namespace)
    api.add_namespace(question_namespace)
