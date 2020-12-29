import requests

from ..settings import envs


def send_menssage(chat_id: str, message: str) -> bool:
    telegram_uri = envs.TELEGRAM_SEND_MESSAGE_URI
    telegram_uri = telegram_uri.replace('%BOT_TOKEN%', envs.TELEGRAM_BOT_TOKEN).replace('%CHAT_ID%', chat_id).replace('%MESSAGE%', message)

    with requests.Session() as session:
        response = session.get(telegram_uri)
        if response.status_code == 200:
            return True
        return False
