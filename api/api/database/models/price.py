from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean, DateTime, func
from sqlalchemy.orm import relationship, backref

from .. import DeclarativeBase, BaseModel


class Price(DeclarativeBase, BaseModel):
    __tablename__ = 'PRICE'

    ID_PRICE = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    ID_WEBSITE = Column(ForeignKey('WEBSITE.ID_WEBSITE', ondelete='CASCADE'), nullable=False, unique=True)
    IN_CASH_PRICE = Column(Float, nullable=True, unique=False)
    INSTALLMENT_PRICE = Column(Float, nullable=True, unique=False)
    REACHED = Column(Boolean, nullable=False, unique=False)
    NOTIFIED = Column(Boolean, nullable=False, unique=False)
    CREATED_AT = Column(DateTime, nullable=False, unique=False, default=func.now())

    website = relationship('WebSite', backref=backref('price', cascade='all,delete', uselist=False))
