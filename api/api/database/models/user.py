from sqlalchemy import Column, Integer, String

from .. import DeclarativeBase, BaseModel


class User(DeclarativeBase, BaseModel):
    __tablename__ = 'USER'

    ID_USER = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    USERNAME = Column(String(64), nullable=False, unique=True)
