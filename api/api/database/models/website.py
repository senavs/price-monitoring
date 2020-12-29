from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, Float
from sqlalchemy.orm import relationship, backref

from .. import DeclarativeBase, BaseModel


class WebSite(DeclarativeBase, BaseModel):
    __tablename__ = 'WEBSITE'

    ID_WEBSITE = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    ID_USER = Column(ForeignKey('USER.ID_USER', ondelete='CASCADE'), nullable=False, unique=False)
    URL = Column(Text, nullable=False, unique=False)
    CSS_SELECTOR_IN_CASH_PRICE = Column(String(256), nullable=False, unique=False)
    CSS_SELECTOR_INSTALLMENT_PRICE = Column(String(256), nullable=False, unique=False)
    IS_BRAZIL_CURRENCY = Column(Boolean, nullable=False, unique=False)
    NOTIFY_GE = Column(Float(2), nullable=True, unique=False)
    NOTIFY_LE = Column(Float(2), nullable=True, unique=False)

    user = relationship('User', backref=backref('websites', cascade='all,delete', lazy='dynamic'))
