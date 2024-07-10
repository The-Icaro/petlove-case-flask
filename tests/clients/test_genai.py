from unittest.mock import MagicMock, patch

import pytest

from src.clients.genai import GenerativeAI


@pytest.fixture
def genai_instance(app):
    with app.app_context():
        genai = GenerativeAI()
        yield genai

@patch('google.generativeai.GenerativeModel')
def test_ask_method(mock_generative_model, genai_instance):
    mock_model_instance = MagicMock()
    mock_generate_content = MagicMock()
    mock_generate_content.text = 'Mocked response'

    mock_model_instance.generate_content.return_value = mock_generate_content
    mock_generative_model.return_value = mock_model_instance

    response = genai_instance.ask('Test question')

    mock_generative_model.assert_called_once()
    assert response == mock_generate_content.text
