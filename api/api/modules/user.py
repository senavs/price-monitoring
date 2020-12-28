from fastapi import HTTPException

from ..database import ClientConnection, User


def list_() -> list[dict]:
    with ClientConnection() as conn:
        users = conn.query(User).order_by(User.ID_USER).all()
        result = [user.to_dict() for user in users]
    return result


def create(username: str) -> dict:
    with ClientConnection() as conn:
        if conn.query(User).filter_by(USERNAME=username).first():
            raise HTTPException(400, 'user already registered')

        user = User(USERNAME=username)
        user.insert(conn)

        result = user.to_dict()
    return result


def delete(id_user: int):
    with ClientConnection() as conn:
        if not (user := User.get(conn, id=id_user)):
            raise HTTPException(404, 'user not registered')

        user.delete(conn)
