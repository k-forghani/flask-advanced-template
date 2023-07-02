from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    SERVER_NAME = environ.get("SERVER_NAME", "127.0.0.1:5000")

    SECRET_KEY = environ.get("SECRET_KEY", "8bf291bfa9e74484bd442bb5b95a0aad")
    FLASK_ENV = environ.get("FLASK_ENV", "development")
    ENV = environ.get("ENV", "development")
    FLASK_APP = environ.get("FLASK_APP", "wsgi.py")
    DEBUG = environ.get("DEBUG", True)
    TESTING = environ.get("TESTING", True)

    ASSETS_DEBUG = environ.get("ASSETS_DEBUG", True)

    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG", True)

    MONGODB_DB = environ.get("MONGODB_DB", "mizan")
    MONGODB_HOST = environ.get("MONGODB_HOST", "localhost")
    MONGODB_PORT = int(environ.get("MONGODB_PORT", 27017))