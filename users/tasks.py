import datetime

import pytz
from celery import shared_task


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
    send_mail('курс', message, EMAIL_HOST_USER, [email])




@shared_task
def last_activity():
    # today = timezone.now().today().date()
    users = User.objects.filter(is_active=True)
    if users.exists():
        for user in users:
            if datetime.datetime.now(
                   pytz.timezone("Europe/Moscow")
            ) - user.last_login > datetime.timedelta(minutes=5):
                user.is_active = False
                user.save()
