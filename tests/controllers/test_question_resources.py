from unittest.mock import patch, MagicMock

@patch('src.controllers.question_controller.QuestionService')
def test_post_question_and_answer(mock_service, client):
    mock_service_instance = MagicMock()
    mock_service_instance.ask_question.return_value = "Mocked response"
    mock_service.return_value = mock_service_instance


    question_data = {
        "question": "Test question",
    }


    response = client.post('/api/ecommerce/v1/question_and_answer/', json=question_data)
    data = response.json

    assert response.status_code == 200
    assert data is not None
    assert data["response"] == "Mocked response"