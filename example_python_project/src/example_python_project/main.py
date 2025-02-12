import os  # Standard library module for interacting with the operating system
import logging  # Standard library module for logging
import subprocess  # Standard library module for running subprocess commands
from flask import Flask  # Import Flask
from example_python_project.config.settings import load_config  # Import app config
from example_python_project.utils.logger import configure_logging  # Import logging setup
from example_python_project.api.flask_app import register_routes  # Import API routes
from example_python_project.middleware.logging_middleware import LoggingMiddleware  # Import logging middleware
import sys  # Import sys for getting Python executable

def start_django():
    """Start the Django development server as a subprocess."""
    django_manage_path = os.path.join(os.path.dirname(__file__), "api/manage.py")  # Get Django's manage.py path
    python_executable = sys.executable  # Get the correct Python executable

    # Get logger instance for this module
    logger = logging.getLogger(__name__)

    # Log the Django startup
    logger.info("Starting Django server on port 8000...")

    try:
        # Run Django server in a subprocess
        subprocess.Popen(
            [python_executable, django_manage_path, "runserver", "0.0.0.0:8000"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        # Log any errors if Django fails to start
        logger.error(f"Failed to start Django server: {e}")

def main():
    """Entry point for the application."""
    # Load environment variables and configurations
    config = load_config()

    # Initialize logging
    configure_logging()
    logger = logging.getLogger(__name__)  # Get logger instance

    # Start Django Server
    start_django()

    # Initialize Flask application
    app = Flask(__name__)  # Create a Flask app instance
    app.config.from_object(config)  # Load configuration settings

    # Apply middleware
    LoggingMiddleware(app)  # Attach logging middleware to Flask app

    # Register API routes
    register_routes(app)  # Register API routes with Flask app

    # Run the Flask application
    port = int(os.getenv("PORT", 5000))  # Get the port number from env variables or default to 5000
    logger.info(f"Starting Flask server on port {port}...")  # Log Flask startup
    app.run(host="0.0.0.0", port=port, debug=config.DEBUG)  # Start Flask server

if __name__ == "__main__":
    main()
