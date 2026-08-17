"""
WSGI entry point for GoDaddy cPanel's "Setup Python App" (Passenger).
Passenger looks for a module named passenger_wsgi.py exposing `application`.
"""
import sys
import os

# Make sure this app's directory is importable
sys.path.insert(0, os.path.dirname(__file__))

from app import app as application  # noqa: E402

if __name__ == "__main__":
    application.run()
