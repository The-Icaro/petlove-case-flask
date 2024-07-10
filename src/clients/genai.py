from logging import getLogger

import google.generativeai as genai
from flask import current_app

logger = getLogger(__name__)

class GenerativeAI:
    __slots__ = ['api_key', 'default_genai_model']

    def __init__(self, genai_model: str = 'gemini-1.5-flash'):
        self.api_key = current_app.config['GENAI_API_KEY']
        self.default_genai_model = genai_model

        genai.configure(api_key=self.api_key)

    def ask(self, query: str) -> str:
        logger.info("Asking question to GenAI model")

        model = genai.GenerativeModel()

        context = "Você é um assistente de vendas do ecommerce Petlove, reponda a seguinte pergunta:"
        response = model.generate_content(context + query)

        logger.info("GenAI generate content completed")

        return response.text
