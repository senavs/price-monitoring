from fastapi import HTTPException

from ..database import ClientConnection, User, Telegram
from ..services.telegram import send_menssage


def list_(username: str) -> list[dict]:
    with ClientConnection() as conn:
        if not (user := conn.query(User).filter_by(USERNAME=username).first()):
            raise HTTPException(404, 'user not registered')
        result = [telegram.to_dict() for telegram in user.telegrams]
    return result


def create(username: str, chat_id: str) -> dict:
    with ClientConnection() as conn:
        if not (user := conn.query(User).filter_by(USERNAME=username).first()):
            raise HTTPException(404, 'user not registered')

        if not send_menssage(chat_id, 'ping'):
            raise HTTPException(404, 'invalid chat id')

        telegram = Telegram(ID_USER=user.ID_USER, CHAT_ID=chat_id)
        telegram.insert(conn)

        result = telegram.to_dict()
    return result


def delete(username: str, id_telegram: int):
    with ClientConnection() as conn:
        if not (user := conn.query(User).filter_by(USERNAME=username).first()):
            raise HTTPException(404, 'user not registered')

        if not (website := user.telegrams.filter_by(ID_TELEGRAM=id_telegram).first()):
            raise HTTPException(400, 'telegram chat not registered for this username')

        website.delete(conn)
