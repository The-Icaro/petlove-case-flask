import os

from flask import current_app as app
from flask import request
from flask_restx import Namespace, Resource, abort, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from src.models.question import PostQuestion, PostQuestionReturn
from src.services.question_service import QuestionService
from src.utils.file import allowed_file

question_namespace = Namespace("question_and_answer", description='Question and answer with OpenAi')
post_question_model = PostQuestion.api_model(question_namespace)
post_question_return_model = PostQuestionReturn.api_model(question_namespace)


upload_parser = reqparse.RequestParser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)
upload_parser.add_argument(*PostQuestion.to_parser(), required=True)

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
        data = PostQuestion.from_dict(request.json)
        return PostQuestionReturn(self.service.ask_question(data.question))


@question_namespace.route('/file_context')
class QuestionFileResource(Resource):
    __slots__ = ['service']

    def __init__(self, *args, **kwargs):
        self.service = QuestionService()
        super().__init__(*args, **kwargs)

    @question_namespace.doc("post_question_and_answer_with_file_context")
    @question_namespace.expect(upload_parser)
    @question_namespace.marshal_with(post_question_return_model)
    def post(self) -> PostQuestionReturn:
        args = upload_parser.parse_args()
        uploaded_file = args['file']

        if not allowed_file(uploaded_file.filename, app.config['ALLOWED_EXTENSIONS']):
            abort(400, 'File type not allowed. Only .txt files are allowed.')

        filename = secure_filename(uploaded_file.filename)

        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(path)

        data = PostQuestion.from_dict(args)
        response = self.service.ask_question_with_file(data.question, path)

        return PostQuestionReturn(response)
