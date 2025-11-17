import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

def transform_data(raw_data: dict) -> pd.DataFrame:
    """
    Recebe um dicionário (JSON da API), normaliza e transforma em DataFrame.
    """
    try:
        df = pd.json_normalize(raw_data)

        # Limpeza e normalização básica
        df.columns = df.columns.str.lower().str.replace(" ", "_")

        # Remover duplicados (idempotência)
        if "id" in df.columns:
            df.drop_duplicates(subset=["id"], inplace=True)

        logger.info(f"Transformação concluída. Registros: {len(df)}")
        return df

    except Exception as e:
        logger.error(f"Erro no processo de transformação: {e}")
        raise
