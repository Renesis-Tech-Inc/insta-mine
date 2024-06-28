from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """
    Settings class to manage application configuration using environment variables.

    Attributes:
        APP_ENV (str): The application environment (default: "development").
        APP_TITLE (str): The application title (default: "InstaMiner - Instagram User Profile Data Miner").
        APP_DESCRIPTION (str): The application description (default: "A tool to fetch Instagram user details.").
        APP_VERSION (str): The application version (default: "1.0.0").
        PORT (int): The port on which the application runs (default: 8000).
    """

    # API Configuration
    APP_ENV: str = Field(default="development", env="APP_ENV")
    APP_TITLE: str = Field(
        default="InstaMiner - Instagram User Profile Data Miner", env="APP_TITLE"
    )
    APP_DESCRIPTION: str = Field(
        default="A tool to fetch Instagram user details.", env="APP_DESCRIPTION"
    )
    APP_VERSION: str = Field(default="1.0.0", env="APP_VERSION")

    PORT: int = Field(default=8000, env="PORT")


# Instantiate the settings
settings = Settings()
