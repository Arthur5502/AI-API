import google.generativeai as genai
from pydantic_settings import BaseSettings
import logging
from datetime import datetime
import pytz

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

    master_prompt = f"""
    Aja como um assistente especialista e prestativo. Sua resposta deve ser clara, bem estruturada e formatada em Markdown.
    
    Regras de formatação:
    - Use **negrito** para destacar termos importantes.
    - Use listas (com marcadores `-` ou numeradas `1.`) para itens, passos ou exemplos.
    - Organize o texto em parágrafos curtos para facilitar a leitura.
    - Se a pergunta for sobre código, utilize blocos de código formatados.

    Contexto adicional: O usuário está no planeta terra. A data atual é {datetime.now(pytz.timezone('America/Recife')).strftime('%d de %B de %Y')}.

    ---

    Pergunta do usuário:
    {prompt}
    """
    
    try:
        response = await model.generate_content_async(master_prompt)
        return response.text.strip()
    except Exception as e:
        logger.error(f"Erro ao se comunicar com a API do Gemini: {e}")
        raise RuntimeError("Falha ao obter resposta do serviço de IA.")