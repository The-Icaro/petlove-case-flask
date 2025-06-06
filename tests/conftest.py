import prometheus_client
import pytest

from src import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "GENAI_API_KEY": "",
        "UPLOAD_FOLDER": "./temp-files-test"
    })

    prometheus_client.REGISTRY = prometheus_client.CollectorRegistry(auto_describe=True)

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
