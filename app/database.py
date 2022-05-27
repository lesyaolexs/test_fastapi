import os

import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DB_HOST = os.environ.get("DB_HOST", "")
db = databases.Database(DB_HOST)

Base = declarative_base()

engine = create_engine(DB_HOST, echo=True)
