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

@patch('google.generativeai.upload_file')
@patch('google.generativeai.get_file')
@patch('google.generativeai.GenerativeModel')
def test_ask_with_file_method(mock_generative_model, mock_get_file, mock_upload_file, genai_instance):
    mock_model_instance = MagicMock()
    mock_generate_content = MagicMock()
    mock_generate_content.text = 'Mocked response'

    mock_uploaded_file = MagicMock()
    mock_uploaded_file.name = 'test.txt'

    mock_upload_file.return_value = mock_uploaded_file

    mock_file = MagicMock()
    mock_get_file.return_value = mock_file

    mock_model_instance.generate_content.return_value = mock_generate_content
    mock_generative_model.return_value = mock_model_instance

    response = genai_instance.ask_with_file('Test question', 'test.txt')

    mock_generative_model.assert_called_once()
    mock_upload_file.assert_called_once_with(path='test.txt', display_name='test.txt', mime_type='text/plain')
    mock_get_file.assert_called_once_with(name='test.txt')
    assert response == mock_generate_content.text
