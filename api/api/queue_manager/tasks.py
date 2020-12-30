from celery import Celery
from requests import HTTPError

from ..database import ClientConnection, WebSite, Price, Telegram
from ..settings import envs
from ..services.telegram import MessagesEnum, send_predefined_message
from ..services.scrapper import get_html, get_element, to_float_currency

app = Celery('price-monitoring', broker=envs.BROKER_URI)


@app.task(name='get_price')
def get_price():
    """"""

    with ClientConnection() as conn:
        skip, limit = 0, 100

        while websites := conn.query(WebSite).offset(skip).limit(limit).all():

            for website in websites:
                if not (price := website.price):
                    price = Price(ID_WEBSITE=website.ID_WEBSITE, IN_CASH_PRICE=None, INSTALLMENT_PRICE=None, REACHED=False, NOTIFIED=False)
                    price.insert(conn)

                try:
                    html = get_html(website.URL)
                except HTTPError:
                    pass
                else:
                    in_cash_price = to_float_currency(get_element(html, website.CSS_SELECTOR_IN_CASH_PRICE), website.IS_BRAZIL_CURRENCY)
                    installment_price = to_float_currency(get_element(html, website.CSS_SELECTOR_INSTALLMENT_PRICE), website.IS_BRAZIL_CURRENCY)

                    if price.IN_CASH_PRICE != float(in_cash_price) or price.INSTALLMENT_PRICE != float(installment_price):
                        price.update(conn, IN_CASH_PRICE=in_cash_price, INSTALLMENT_PRICE=installment_price, REACHED=True, NOTIFIED=False)

                send_message(price.ID_PRICE)

            skip += limit


@app.task(name='send_message')
def send_message(id_price: int):
    with ClientConnection() as conn:
        price = Price.get(conn, id=id_price)
        website = price.website

        if price.NOTIFIED:
            return

        notify_ge, notify_le = price.website.NOTIFY_GE, price.website.NOTIFY_LE

        for chat_id, *_ in conn.query(Telegram.CHAT_ID).filter_by(ID_USER=website.ID_USER).all():
            notified = False

            # notify if price is less or equal
            if notify_le is not None:
                if price.IN_CASH_PRICE and price.IN_CASH_PRICE <= notify_le:
                    send_predefined_message(chat_id, MessagesEnum.IN_CASH_LE, url=website.URL, price=price.IN_CASH_PRICE, notify_price=notify_le)
                    notified = True
                if price.INSTALLMENT_PRICE and price.INSTALLMENT_PRICE <= notify_le:
                    send_predefined_message(chat_id, MessagesEnum.INSTALLMENT_LE, url=website.URL, price=price.INSTALLMENT_PRICE, notify_price=notify_le)
                    notified = True

            # notify if price is greater or equal
            if notify_ge is not None:
                if price.IN_CASH_PRICE and price.IN_CASH_PRICE >= notify_ge:
                    send_predefined_message(chat_id, MessagesEnum.IN_CASH_GE, url=website.URL, price=price.IN_CASH_PRICE, notify_price=notify_ge)
                    notified = True
                if price.INSTALLMENT_PRICE and price.INSTALLMENT_PRICE >= notify_ge:
                    send_predefined_message(chat_id, MessagesEnum.INSTALLMENT_GE, url=website.URL, price=price.INSTALLMENT_PRICE, notify_price=notify_ge)
                    notified = True

            if notified:
                price.update(conn, NOTIFIED=True)
