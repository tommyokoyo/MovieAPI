from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_uri = 'postgresql://okoyo:password@localhost/movies_db'
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()
