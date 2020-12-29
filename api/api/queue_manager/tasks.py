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
                # get website config information
                id_website = website.ID_WEBSITE
                url = website.URL
                css_selector_in_cash = website.CSS_SELECTOR_IN_CASH_PRICE
                css_selector_installment = website.CSS_SELECTOR_INSTALLMENT_PRICE
                is_brazil_currency = website.IS_BRAZIL_CURRENCY

                # do scrapper
                try:
                    html = get_html(url)
                except HTTPError:
                    price = Price(ID_WEBSITE=id_website, IN_CASH_PRICE=0., INSTALLMENT_PRICE=0., ACCESSED=False)
                    price.insert(conn)
                else:
                    in_cash_price = to_float_currency(get_element(html, css_selector_in_cash), is_brazil_currency)
                    installment_price = to_float_currency(get_element(html, css_selector_installment), is_brazil_currency)
                    price = Price(ID_WEBSITE=id_website, IN_CASH_PRICE=in_cash_price, INSTALLMENT_PRICE=installment_price, ACCESSED=True)

                price.insert(conn)
                send_message(price.ID_PRICE)

            skip += limit


@app.task(name='send_message')
def send_message(id_price: int):
    with ClientConnection() as conn:
        if not (price := Price.get(conn, id=id_price)):
            return

        url = price.website.URL
        id_user = price.website.ID_USER
        notify_ge, notify_le = price.website.NOTIFY_GE, price.website.NOTIFY_LE

        for telegram in conn.query(Telegram).filter_by(ID_USER=id_user).all():
            chat_id = telegram.CHAT_ID

            # notify if price is less or equal
            if notify_le is not None:
                if price.IN_CASH_PRICE <= notify_le:
                    send_predefined_message(chat_id, MessagesEnum.IN_CASH_LE, url=url, price=price.IN_CASH_PRICE, notify_price=notify_le)
                if price.INSTALLMENT_PRICE <= notify_le:
                    send_predefined_message(chat_id, MessagesEnum.INSTALLMENT_LE, url=url, price=price.INSTALLMENT_PRICE, notify_price=notify_le)

            # notify if price is greater or equal
            if notify_ge is not None:
                if price.IN_CASH_PRICE >= notify_ge:
                    send_predefined_message(chat_id, MessagesEnum.IN_CASH_GE, url=url, price=price.IN_CASH_PRICE, notify_price=notify_ge)
                if price.INSTALLMENT_PRICE >= notify_ge:
                    send_predefined_message(chat_id, MessagesEnum.INSTALLMENT_GE, url=url, price=price.INSTALLMENT_PRICE, notify_price=notify_ge)
