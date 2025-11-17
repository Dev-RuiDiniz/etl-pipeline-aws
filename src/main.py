from extract.extractor import extract_data
from transform.transformer import transform_data
from load.loader import load_data
from utils.aws import save_to_s3
from utils.logger import get_logger

logger = get_logger(__name__)

def run_pipeline():
    logger.info("Iniciando pipeline ETL...")

    raw = extract_data()
    save_to_s3(raw, prefix="raw/")

    df = transform_data(raw)
    save_to_s3(df.to_dict(orient="records"), prefix="processed/")

    load_data(df)

    logger.info("Pipeline finalizado com sucesso.")

if __name__ == "__main__":
    run_pipeline()
