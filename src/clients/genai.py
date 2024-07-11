from logging import getLogger

import google.generativeai as genai
from flask import current_app

from src.utils.consts import GEN_AI_CONTEXT, GEN_AI_MODEL

logger = getLogger(__name__)

class GenerativeAI:
    __slots__ = ['api_key', 'default_genai_model']

    def __init__(self, genai_model: str = GEN_AI_MODEL):
        self.api_key = current_app.config['GENAI_API_KEY']
        self.default_genai_model = genai_model

        genai.configure(api_key=self.api_key)

    def ask(self, query: str) -> str:
        logger.info("Asking question to GenAI model")

        model = genai.GenerativeModel()
        response = model.generate_content(GEN_AI_CONTEXT + query)

        logger.info("GenAI generate content completed")

        return response.text

    def ask_with_file(self, query: str, file_path: str) -> str:
        logger.info("Asking question to GenAI model with file")

        model = genai.GenerativeModel()

        filename = file_path.split('/')[-1]
        uploaded_file = genai.upload_file(path=file_path, display_name=filename, mime_type="text/plain")

        file = genai.get_file(name=uploaded_file.name)
        response = model.generate_content([GEN_AI_CONTEXT + query, file])

        logger.info("GenAI generate content with file completed")

        return response.text
