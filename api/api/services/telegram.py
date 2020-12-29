from enum import Enum

import requests

from ..settings import envs


class MessagesEnum(Enum):
    IN_CASH_LE: str = 'Hey!! Produto mais barato, corre lá!\n\nProduto: {url}\nValor à vista: {price}\nValor desejado informado: {notify_price}'
    IN_CASH_GE: str = 'Vixii!! Produto ficou mais caro\n\nProduto: {url}\nValor à vista: {price}\nValor desejado informado: {notify_price}'

    INSTALLMENT_LE: str = 'Opaa! Produto mais barato no cartão\n\nProduto: {url}\nValor parcelado: {price}\nValor desejado informado: {notify_price}'
    INSTALLMENT_GE: str = 'Aném :( Produto ficou mais caro\n\nProduto: {url}\nValor parcelado: {price}\nValor desejado informado: {notify_price}'


def send_menssage(chat_id: str, message: str) -> bool:
    telegram_uri = envs.TELEGRAM_SEND_MESSAGE_URI
    telegram_uri = telegram_uri.replace('%BOT_TOKEN%', envs.TELEGRAM_BOT_TOKEN).replace('%CHAT_ID%', chat_id).replace('%MESSAGE%', message)

    with requests.Session() as session:
        response = session.get(telegram_uri)
        if response.status_code == 200:
            return True
        return False


def send_predefined_message(chat_id: str, message_type: MessagesEnum, *, url: str, price: float, notify_price: float) -> bool:
    message = message_type.value.format(url=url, price=price, notify_price=notify_price)
    return send_menssage(chat_id, message)
