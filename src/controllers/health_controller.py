from flask_restx import Namespace, Resource

health_namespace = Namespace("health", description='Health check operations')

@health_namespace.route('')
class HealthResource(Resource):
    @health_namespace.doc("get_health")
    def get(self):
        return {"status": "up"}
