import logging  # Standard Python logging module
import os  # Provides access to environment variables

def configure_logging():
    """Configures logging settings based on the environment."""
    
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()  # Get log level from environment, default to INFO
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Define log format
    log_date_format = "%Y-%m-%d %H:%M:%S"  # Set timestamp format

    # Configure logging globally
    logging.basicConfig(
        level=log_level,  # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format=log_format,  # Define logging format
        datefmt=log_date_format,  # Set timestamp format
        handlers=[
            logging.StreamHandler(),  # Log messages to console
        ]
    )

    # Suppress overly verbose logs from third-party libraries
    logging.getLogger("werkzeug").setLevel(logging.WARNING)  # Reduce Flask request logs
    logging.getLogger("sqlalchemy").setLevel(logging.WARNING)  # Reduce SQLAlchemy logs
