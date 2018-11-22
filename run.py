"""Manages the app to run properly."""
import os

from app import app

# Start the app and set the environment
# config_name = os.getenv('FLASK_ENV')
# app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)
