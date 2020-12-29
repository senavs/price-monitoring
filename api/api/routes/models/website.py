from pydantic import BaseModel


class Website(BaseModel):
    id_website: int
    id_user: int
    url: str
    css_selector_in_cash_price: str
    css_selector_installment_price: str
    is_brazil_currency: bool


class WebsiteResponseList(BaseModel):
    """Response model to /websites/{username}/list"""

    result: list[Website]


class WebsiteResponseCreate(BaseModel):
    """Response model to /websites/{username}/create"""

    result: Website


class WebsiteRequestCreate(BaseModel):
    """Request model to /websites/{username}/create"""

    url: str
    css_selector_in_cash_price: str
    css_selector_installment_price: str
    is_brazil_currency: bool = True
