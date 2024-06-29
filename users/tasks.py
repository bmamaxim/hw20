import datetime
import requests
import pytz
from celery import shared_task
from config import settings

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from users.models import User


@shared_task
def send_direction_create(email, message):
    """
    Функция отправляет сообщение на почту.
    :param email:
    :param message:
    :return:
    """
    print(email)
    send_mail("курс", message, EMAIL_HOST_USER, email)


@shared_task
def send_telegram_message(chat_id, message):
    """
    Функция отправки сообщений в телеграмм.
    """
    print(chat_id)
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/sendMessage', params=params)

@shared_task
def last_activity():
    # today = timezone.now().today().date()
    users = User.objects.filter(is_active=True)
    if users.exists():
        for user in users:
            if datetime.datetime.now(
                    pytz.timezone("Europe/Moscow")
            ) - user.last_login > datetime.timedelta(days=30):
                user.is_active = False
                user.save()
