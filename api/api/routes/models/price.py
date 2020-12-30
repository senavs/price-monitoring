from datetime import datetime

from pydantic import BaseModel


class Price(BaseModel):
    id_price: int
    id_website: int
    in_cash_price: float
    installment_price: float
    notified: bool
    reached: bool
    created_at: datetime


class PriceResponseList(BaseModel):
    """Response model to /price/{username}/{id_website}/list"""

    result: Price
