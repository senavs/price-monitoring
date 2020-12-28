from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref

from .. import DeclarativeBase, BaseModel


class Telegram(DeclarativeBase, BaseModel):
    __tablename__ = 'TELEGRAM'

    ID_TELEGRAM = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    ID_USER = Column(ForeignKey('USER.ID_USER', ondelete='CASCADE'), nullable=False, unique=False)
    TOKEN = Column(String(64), nullable=False, unique=False)
    CHAT_ID = Column(Integer, nullable=False, unique=False)

    user = relationship('User', backref=backref('telegrams', cascade='delete;all'))