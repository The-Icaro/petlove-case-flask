import pytest
import prometheus_client

from src import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "GENAI_API_KEY": "",
    })

    prometheus_client.REGISTRY = prometheus_client.CollectorRegistry(auto_describe=True)

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
