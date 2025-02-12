from flask import Flask, request  # Import Flask framework and request object
import logging  # Import logging module for capturing logs

class LoggingMiddleware:
    """Middleware to log requests and responses."""

    def __init__(self, app: Flask):
        """Initialize middleware and attach request logging."""
        self.app = app  # Store reference to the Flask app
        self.app.before_request(self.log_request)  # Register log_request function to run before each request

    def log_request(self):
        """Logs incoming HTTP requests before processing."""
        logging.info(f"Request: {request.method} {request.path}")  # Log HTTP method and request path
