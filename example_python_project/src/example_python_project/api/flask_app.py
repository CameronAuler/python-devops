from flask import Flask  # Import Flask framework

def register_routes(app: Flask):
    """Register API routes with the Flask app."""
    
    @app.route("/health", methods=["GET"])  # Define a health check route at "/health"
    def health_check():
        """Simple health check endpoint to verify server status."""
        return {"status": "OK"}, 200  # Return a JSON response with HTTP 200 status
