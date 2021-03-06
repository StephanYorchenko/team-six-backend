import sqlalchemy
from databases import Database

from settings import *

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
db = Database(DATABASE_URL, min_size=1, max_size=3)

metadata = sqlalchemy.MetaData()
