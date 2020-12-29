from fastapi import HTTPException

from ..database import ClientConnection, User


def list_(username: str, id_website: int) -> list[dict]:
    with ClientConnection() as conn:
        if not (user := conn.query(User).filter_by(USERNAME=username).first()):
            raise HTTPException(404, 'user not registered')
        if not (website := user.websites.filter_by(ID_WEBSITE=id_website).first()):
            raise HTTPException(400, 'website not registered for this username')

        result = [price.to_dict() for price in website.prices]
    return result
