from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean, DateTime, func
from sqlalchemy.orm import relationship, backref

from .. import DeclarativeBase, BaseModel


class Price(DeclarativeBase, BaseModel):
    __tablename__ = 'PRICE'

    ID_PRICE = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    ID_WEBSITE = Column(ForeignKey('WEBSITE.ID_WEBSITE', ondelete='CASCADE'), nullable=False, unique=False)
    IN_CASH_PRICE = Column(Float, nullable=False, unique=False)
    INSTALLMENT_PRICE = Column(Float, nullable=False, unique=False)
    ACCESSED = Column(Boolean, nullable=False, unique=False)
    CREATED_AT = Column(DateTime, nullable=False, unique=False, default=func.now())

    website = relationship('WebSite', backref=backref('prices', cascade='delete;all'))
