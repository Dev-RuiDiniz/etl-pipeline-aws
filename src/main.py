from extract.extractor import extract_data
from transform.transformer import transform_data
from load.loader import load_data
from utils.aws import save_to_s3
from utils.logger import get_logger

logger = get_logger(__name__)

def run_pipeline():
    logger.info("Iniciando pipeline ETL...")

    # Extração
    raw_data = extract_data()
    save_to_s3(raw_data, prefix="raw/")

    # Transformação
    df = transform_data(raw_data)

    # Auditoria: salva dataset transformado
    save_to_s3(df.to_dict(orient="records"), prefix="processed/")

    # Load
    load_data(df)

    logger.info("Pipeline finalizado com sucesso.")

if __name__ == "__main__":
    run_pipeline()
