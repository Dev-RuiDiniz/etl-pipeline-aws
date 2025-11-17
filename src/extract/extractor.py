import requests
from utils.logger import get_logger
from config.settings import settings

logger = get_logger(__name__)

def extract_data() -> dict:
    """
    Extrai dados da API pública definida no .env / settings.py.
    """
    url = settings.API_URL

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        logger.info("Extração concluída com sucesso.")
        return response.json()

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao extrair dados da API: {e}")
        raise
