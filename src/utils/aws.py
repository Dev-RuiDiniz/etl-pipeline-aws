import boto3
import json
import datetime
from botocore.exceptions import ClientError
from config.settings import settings
from utils.logger import get_logger

logger = get_logger(__name__)
s3 = boto3.client("s3", region_name=settings.AWS_REGION)

def save_to_s3(content, prefix="raw/"):
    try:
        timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        key = f"{prefix}{timestamp}.json"

        s3.put_object(
            Bucket=settings.S3_BUCKET,
            Key=key,
            Body=json.dumps(content),
            ContentType="application/json"
        )
        logger.info(f"Arquivo salvo em S3: {key}")

    except ClientError as e:
        logger.error(f"Erro ao salvar em S3: {e}")
        raise
