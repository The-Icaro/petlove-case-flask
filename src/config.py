import os


class Config:
    GENAI_API_KEY = os.environ.get('GENAI_API_KEY')
    UPLOAD_FOLDER="./files"
    MAX_CONTENT_LENGTH=16 * 1024 * 1024
    ALLOWED_EXTENSIONS=["txt"]
