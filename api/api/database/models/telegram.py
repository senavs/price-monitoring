from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref

from .. import DeclarativeBase, BaseModel


class Telegram(DeclarativeBase, BaseModel):
    __tablename__ = 'TELEGRAM'

    ID_TELEGRAM = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    ID_USER = Column(ForeignKey('USER.ID_USER', ondelete='CASCADE'), nullable=False, unique=False)
    CHAT_ID = Column(String(32), nullable=False, unique=False)

    user = relationship('User', backref=backref('telegrams', cascade='all,delete', lazy='dynamic'))
