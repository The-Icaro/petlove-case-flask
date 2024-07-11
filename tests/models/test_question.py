from unittest.mock import Mock

from src.models.question import PostQuestion, PostQuestionReturn


def test_base_post_question():
    post_question = PostQuestion('Test')
    assert post_question.question == 'Test'

def test_from_dict_post_question():
    post_question = PostQuestion.from_dict({'question': 'Test'})
    assert post_question.question == 'Test'

def test_to_parser_post_question():
    post_question_parser = PostQuestion.to_parser()
    assert post_question_parser.get('question') is not None

def test_api_model_post_question():
    api = Mock()
    api.model = Mock()

    api.model.return_value = PostQuestion('Test')

    post_question = PostQuestion.api_model(api)

    api.model.assert_called_once()
    assert post_question.question == 'Test'

def test_base_post_question_return():
    post_question_return = PostQuestionReturn('Test')
    assert post_question_return.response == 'Test'

def test_api_model_post_question_return():
    api = Mock()
    api.model = Mock()

    api.model.return_value = PostQuestionReturn('Test')

    post_question_return = PostQuestionReturn.api_model(api)

    api.model.assert_called_once()
    assert post_question_return.response == 'Test'
