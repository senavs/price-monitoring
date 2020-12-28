from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, backref

from .. import DeclarativeBase, BaseModel


class WebSite(DeclarativeBase, BaseModel):
    __tablename__ = 'WEBSITE'

    ID_WEBSITE = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    ID_USER = Column(ForeignKey('USER.ID_USER', ondelete='CASCADE'), nullable=False, unique=False)
    URL = Column(Text, nullable=False, unique=False)
    XPATH_IN_CASH_PRICE = Column(String(256), nullable=False, unique=False)
    XPATH_INSTALLMENT_PRICE = Column(String(256), nullable=False, unique=False)

    user = relationship('User', backref=backref('websites', cascade='delete;all'))
