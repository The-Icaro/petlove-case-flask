from logging import getLogger

from src.clients.genai import GenerativeAI

logger = getLogger(__name__)

class QuestionService:
    __slots__ = ['genai_client']

    def __init__(self, genai_client: GenerativeAI = None):
        self.genai_client = genai_client or GenerativeAI()

    def ask_question(self, question: str) -> str:
        logger.info(f"Asking question: {question}")
        return self.genai_client.ask(question)

    def ask_question_with_file(self, question: str, file_path: str) -> str:
        logger.info(f"Asking question with file: {question}")
        return self.genai_client.ask_with_file(question, file_path)
