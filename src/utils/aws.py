import boto3
from utils.logger import get_logger
from config.settings import settings
from botocore.exceptions import ClientError
import json
import datetime

logger = get_logger(__name__)

s3 = boto3.client("s3", region_name=settings.AWS_REGION)

def save_to_s3(content: dict, prefix: str = "raw/"):
    """
    Salva um JSON no S3 com timestamp.
    """
    try:
        timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        key = f"{prefix}{timestamp}.json"
        
        s3.put_object(
            Bucket=settings.S3_BUCKET,
            Key=key,
            Body=json.dumps(content),
            ContentType="application/json"
        )
        logger.info(f"Arquivo salvo no S3: {key}")
    
    except ClientError as e:
        logger.error(f"Erro ao salvar arquivo no S3: {e}")
        raise
