"""Configuration module for application settings.

This module provides configuration management using Pydantic BaseSettings
to handle environment variables and configuration values.
"""

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Configuration settings class that loads environment variables.

    Inherits from BaseSettings to automatically read configuration from environment
    variables and .env files.
    """

    DATABASE_URL: str
    REDIS_URL: str
    RABBITMQ_URL: str

    class Config:
        """Inner configuration class for Settings.

        Specifies configuration options for the Settings class, including the
        environment file location.
        """

        env_file = ".env"


settings = Settings()
