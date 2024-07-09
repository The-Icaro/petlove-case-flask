from flask_restx import Api


from src.controllers.health_controller import health_namespace


def register_namespaces(api: Api):
    api.add_namespace(health_namespace)
