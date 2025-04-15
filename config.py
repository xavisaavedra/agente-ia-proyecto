# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # Carga automática desde .env en raíz del proyecto

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PDF_DIR = "./data/documents/"

    @staticmethod
    def validate_config():
        if not Config.OPENAI_API_KEY:
            raise ValueError("API_KEY no encontrada en variables de entorno")

