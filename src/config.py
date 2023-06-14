import os
from dotenv import load_dotenv
from pathlib import Path  # Python3 only
from os.path import join, dirname
from os.path import join, dirname

# Load enviorment variables
# Windows
dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path)

class Config:
    """
    Set configuration vars from .env file
    """
    # Pyra Version
    PYRA_VERSION = "v0.0.1"

    # Load in environment variables
    # These fields are associated with logger
    LOG_DIR = os.getenv('LOG_DIR')
    LOG_FORMAT = os.getenv('LOG_FORMAT')

    # mongo credential
    MONGO_USERNAME = os.getenv('MONGO_USERNAME')
    MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
    MONGO_HOST = os.getenv('MONGO_HOST')
    MONGO_PORT = os.getenv('MONGO_PORT')
    MONGO_DATABASE = os.getenv('MONGO_DATABASE')
    MONGO_COLLECTION = os.getenv('MONGO_COLLECTION')

    # data
    DATA_DIR = os.getenv('DATA_DIR') 
