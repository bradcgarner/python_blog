import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import app
# ??? this looks in current directory for files that have an app object?
# ??? works because app is in __init__ ???

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URL'])

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#  basic boilerplate code for working with a database using SQLAlchemy. You create the engine which will talk to the database at the database URI which you specified in the config. You then create a declarative base, and start a new session.

class Entry(Base):
  __tablename__ = 'entries'
  id = Column(Integer, primary_key=True)
  title = Column(String(1024))
  content = Column(Text)
  datetime = Column(DateTime, default=datetime.datetime.now)

Base.metadata.create_all(engine)

