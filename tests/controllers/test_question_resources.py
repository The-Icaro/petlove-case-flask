import os
import tempfile
from unittest.mock import MagicMock, patch
import shutil


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


@patch('src.controllers.question_controller.QuestionService')
def test_post_question_and_answer_with_file(mock_service, client):
    mock_service_instance = MagicMock()
    mock_service_instance.ask_question_with_file.return_value = "Mocked response"
    mock_service.return_value = mock_service_instance

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    temp_file.write(b'Test file')
    temp_file.seek(0)
    temp_file.close()

    route = '/api/ecommerce/v1/question_and_answer/file_context'

    try:
      with open(temp_file.name, 'rb') as file:
          data = {
              'file': (file, temp_file.name)
          }
          response = client.post(route, data=data, content_type='multipart/form-data')

      data = response.json

      assert response.status_code == 200
      assert data is not None
      assert data["response"] == mock_service_instance.ask_question_with_file.return_value
    finally:
        remove_files_in_directory("./temp-files-test")

@patch('src.controllers.question_controller.QuestionService')
def test_error_post_question_and_answer_with_file(mock_service, client):
    mock_service_instance = MagicMock()
    mock_service_instance.ask_question_with_file.return_value = "Mocked response"
    mock_service.return_value = mock_service_instance

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(b'Test file')
    temp_file.seek(0)
    temp_file.close()

    route = '/api/ecommerce/v1/question_and_answer/file_context'

    with open(temp_file.name, 'rb') as file:
        data = {
            'file': (file, temp_file.name)
        }
        response = client.post(route, data=data, content_type='multipart/form-data')

    assert response.status_code == 400
    assert b'File type not allowed. Only .txt files are allowed.' in response.data


def remove_files_in_directory(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Error {e}")