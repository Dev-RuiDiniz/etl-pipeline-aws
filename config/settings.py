from pydantic import BaseSettings, AnyHttpUrl, Field

class Settings(BaseSettings):
    # API
    API_URL: AnyHttpUrl = Field(..., env="API_URL")

    # Database
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_NAME: str = Field(..., env="DB_NAME")
    DB_PORT: int = Field(5432, env="DB_PORT")

    # AWS
    AWS_REGION: str = Field("us-east-1", env="AWS_REGION")
    S3_BUCKET: str = Field(..., env="S3_BUCKET")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
