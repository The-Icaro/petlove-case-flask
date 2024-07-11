from unittest.mock import MagicMock

import pytest

from src.services.question_service import QuestionService


@pytest.fixture
def mock_genai_client():
    return MagicMock()

@pytest.fixture
def question_service(mock_genai_client):
    return QuestionService(genai_client=mock_genai_client)

def test_ask_question(question_service, mock_genai_client):
    question = "Test question"
    response = question_service.ask_question(question)


    assert response == mock_genai_client.ask.return_value
    mock_genai_client.ask.assert_called_once_with(question)

def test_ask_question_with_file(question_service, mock_genai_client):
    question = "Test question"
    file_path = "test.txt"
    response = question_service.ask_question_with_file(question, file_path)

    assert response == mock_genai_client.ask_with_file.return_value
    mock_genai_client.ask_with_file.assert_called_once_with(question, file_path)
