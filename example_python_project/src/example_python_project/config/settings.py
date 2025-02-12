import os  # Provides access to system environment variables
from dotenv import load_dotenv  # Loads environment variables from a .env file

# Load environment variables from .env file if available
load_dotenv()

class Config:
    """Base configuration class that loads environment variables and default settings."""

    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")  # Enable debug mode if set to True
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")  # Application secret key for encryption and sessions
    PORT = int(os.getenv("PORT", 5000))  # Port number for the application server

    # Database settings
    DB_HOST = os.getenv("DB_HOST", "localhost")  # Database hostname
    DB_PORT = int(os.getenv("DB_PORT", 5432))  # Database port number (default: PostgreSQL)
    DB_NAME = os.getenv("DB_NAME", "example_db")  # Database name
    DB_USER = os.getenv("DB_USER", "user")  # Database username
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")  # Database password

    # Logging settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # Logging level (e.g., DEBUG, INFO, WARNING, ERROR)

    # Caching configuration
    CACHE_TYPE = os.getenv("CACHE_TYPE", "simple")  # Caching backend (options: redis, memcached, simple)

def load_config():
    """Returns an instance of the Config class to be used in the application."""
    return Config()
