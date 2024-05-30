import datetime

from celery import shared_task
from django.utils import timezone

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
    print('today')
    #today = timezone.now().today().date()

    #users = User.objects.filter(is_active=True)
    ##if today - user.date_joined > datetime.timedelta(minutes=2):
            #user.is_active = False
            #user.save()
