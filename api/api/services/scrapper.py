import re
from decimal import Decimal

import requests
from bs4 import BeautifulSoup

RE_BR_CURRENCY = re.compile(r'[^\d,]')
RE_US_CURRENCY = re.compile(r'[^\d.]')


def get_html(url: str) -> str:
    """Get HTML page from an URL"""

    with requests.Session() as session:
        response = session.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        })
        if not 200 <= response.status_code < 300:
            response.raise_for_status()

    return response.text


def get_element(html: str, css_selector: str) -> str:
    """Get tag text from HTML page using CSS selector"""

    soup = BeautifulSoup(html, 'html.parser')
    element = soup.select_one(css_selector)
    if element:
        return element.text
    return ''


def to_float_currency(currency: str, brazil_currency: bool = True) -> Decimal:
    if not currency:
        return Decimal('0.')
    if brazil_currency:
        currency = RE_BR_CURRENCY.sub('', currency)
        currency = re.sub(r',', '.', currency)
    else:
        currency = RE_US_CURRENCY.sub('', currency)
    return Decimal(currency)
