from starlette.config import Config
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from databases import Database

import sqlalchemy

config = Config('.env')
DATABASE_URL = config('DATABASE_URL')

middleware = [
  Middleware(CORSMiddleware, allow_origins=['*'])
]

metadata = sqlalchemy.MetaData()
database = Database(DATABASE_URL)