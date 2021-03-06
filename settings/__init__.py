import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / 'settings/.env')

# Database

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = 5432

# OpenAPI

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
AS_URL = os.getenv('AS_URL')
RS_PS_URL = os.getenv('RS_PS_URL')
AS_AUTH_URL = os.getenv('AS_AUTH_URL')
REDIRECT_URI = os.getenv('REDIRECT_URI')
