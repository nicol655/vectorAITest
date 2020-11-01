from starlette.config import Config
from databases import Database

import sqlalchemy


config = Config('.env')
DATABASE_URL = config('DATABASE_URL')

metadata = sqlalchemy.MetaData()
database = Database(DATABASE_URL)