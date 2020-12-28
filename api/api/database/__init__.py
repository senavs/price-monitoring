from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from ..settings import envs

engine = create_engine(envs.DATABASE_URI, echo=False)
DeclarativeBase = declarative_base()
Session = sessionmaker(engine)

from .core import *  # noqa
from .models import *  # noqa
