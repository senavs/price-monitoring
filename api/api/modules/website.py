from fastapi import HTTPException

from ..database import ClientConnection, User, WebSite


def list_(username: str) -> list[dict]:
    with ClientConnection() as conn:
        if not (user := conn.query(User).filter_by(USERNAME=username).first()):
            raise HTTPException(404, 'user not registered')
        result = [website.to_dict() for website in user.websites]
    return result


def create(username: str, url: str, css_selector_in_cash_price: str, css_selector_installment_price: str, is_brazil_currency: bool = True,
           notify_ge: float = None, notify_le: float = None) -> dict:
    with ClientConnection() as conn:
        if not (user := conn.query(User).filter_by(USERNAME=username).first()):
            raise HTTPException(404, 'user not registered')

        website = WebSite(ID_USER=user.ID_USER, URL=url,
                          CSS_SELECTOR_IN_CASH_PRICE=css_selector_in_cash_price, CSS_SELECTOR_INSTALLMENT_PRICE=css_selector_installment_price,
                          IS_BRAZIL_CURRENCY=is_brazil_currency, NOTIFY_GE=notify_ge, NOTIFY_LE=notify_le)
        website.insert(conn)

        result = website.to_dict()
    return result


def delete(username: str, id_website: int):
    with ClientConnection() as conn:
        if not (user := conn.query(User).filter_by(USERNAME=username).first()):
            raise HTTPException(404, 'user not registered')

        if not (website := user.websites.filter_by(ID_WEBSITE=id_website).first()):
            raise HTTPException(400, 'website not registered for this username')

        website.delete(conn)
