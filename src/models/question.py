from flask_restx import fields


class PostQuestion:
    __slots__ = ['question']

    def __init__(self, question):
        self.question = question

    @staticmethod
    def api_model(api):
        return api.model('PostQuestion', {
            'question': fields.String(required=True, description='The question text')
        })

    @staticmethod
    def to_parser():
        return {'question': fields.String(required=True, description='The question text')}

    @staticmethod
    def from_dict(data):
        return PostQuestion(data['question'])

class PostQuestionReturn:
    __slots__ = ['response']

    def __init__(self, response):
        self.response = response

    @staticmethod
    def api_model(api):
        return api.model('PostQuestionReturn', {
            'response': fields.String(required=True, description='The response text')
        })
