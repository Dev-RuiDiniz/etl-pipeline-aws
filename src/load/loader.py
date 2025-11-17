import pandas as pd
from sqlalchemy import create_engine
from utils.logger import get_logger
from config.settings import settings

logger = get_logger(__name__)

def get_engine():
    """
    Cria engine SQLAlchemy para conexão com PostgreSQL (RDS).
    """
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}"
            f"@{settings.DB_HOST}/{settings.DB_NAME}"
        )
        return engine
    except Exception as e:
        logger.error(f"Erro ao criar engine do banco: {e}")
        raise

def load_data(df: pd.DataFrame, table_name: str = "etl_data"):
    """
    Carrega os dados no PostgreSQL usando SQLAlchemy.
    Usa upsert básico (replace full table ou append).
    """
    engine = get_engine()

    try:
        df.to_sql(table_name, engine, if_exists="append", index=False)
        logger.info(f"Load concluído: {len(df)} registros inseridos.")
    except Exception as e:
        logger.error(f"Erro ao carregar dados no banco: {e}")
        raise
