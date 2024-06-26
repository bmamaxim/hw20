import stripe

from config.settings import STRIPE_API_KEY
from forex_python.converter import CurrencyRates


stripe.api_key = STRIPE_API_KEY


def convert_rub_to_usd(amount):
    """
    Функция конвертации валюты
    рубли в доллары.
    https://forex-python.readthedocs.io/en/latest/usage.html
    :param amount:
    :return:
    """
    # c = CurrencyRates()
    rate = CurrencyRates().get_rate("RUB", "USD")
    return int(amount * rate)


def create_stripe_product(direction):
    """
    Функция названия продукта оплаты
    :param direction:
    :return:
    """
    return stripe.Product.create(name=direction.title_direction)


def create_stripe_price(amount, product):
    """
    Функция создания цены в страйп.
    :param product:
    :param amount: int
    :return:
    """

    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": product},
    )


def create_stripe_session(price):
    """
    Функция создает сессию на оплату в страйп.
    :param price:
    :return:
    """
    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
