import google.generativeai as genai
from pydantic_settings import BaseSettings
import logging

class Settings(BaseSettings):
    google_api_key: str

    class Config:
        env_file = ".env"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    settings = Settings()
    genai.configure(api_key=settings.google_api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    logger.info("Modelo de IA inicializado com sucesso.")
except Exception as e:
    logger.error(f"Erro ao inicializar o modelo de IA: {e}")
    model = None

async def get_ai_response(prompt: str) -> str:
    if not model:
        raise ConnectionError("O modelo de IA não foi inicializado corretamente.")
    
    try:
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Erro ao se comunicar com a API do Gemini: {e}")
        raise RuntimeError("Falha ao obter resposta do serviço de IA.")