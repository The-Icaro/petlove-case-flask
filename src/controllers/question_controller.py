from flask import request
from flask_restx import Namespace, Resource

from src.models.question import PostQuestion, PostQuestionReturn
from src.services.question_service import QuestionService

question_namespace = Namespace("question_and_answer", description='Question and answer with OpenAi')
post_question_model = PostQuestion.api_model(question_namespace)
post_question_return_model = PostQuestionReturn.api_model(question_namespace)


@question_namespace.route('/')
class QuestionResource(Resource):
    __slots__ = ['service']

    def __init__(self, *args, **kwargs):
        self.service = QuestionService()
        super().__init__(*args, **kwargs)

    @question_namespace.doc("post_question_and_answer")
    @question_namespace.expect(post_question_model)
    @question_namespace.marshal_with(post_question_return_model)
    def post(self) -> PostQuestionReturn:
        question_data = request.json
        question = PostQuestion.from_dict(question_data)

        return PostQuestionReturn(self.service.ask_question(question.question))
