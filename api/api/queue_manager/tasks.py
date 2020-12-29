from celery import Celery
from requests import HTTPError

from ..database import ClientConnection, WebSite, Price
from ..settings import envs
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

            skip += limit
