from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Direction, Lesson

NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='элктронная почта')
    avatar = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    phone = models.CharField(max_length=200, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=200, verbose_name='страна', **NULLABLE)
    ver_code = models.CharField(max_length=4, verbose_name='код верификации', **NULLABLE)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'



    def __str__(self):
        return f"{self.email} {self.phone} {self.country}"


class Payment(models.Model):
    PAY_CASH = 'cash'
    PAY_NON_CASH = 'non-cash'

    PAY_METHOD = (
        (PAY_CASH, 'наличный'),
        (PAY_NON_CASH, 'безнал'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='студент', **NULLABLE)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='урок', **NULLABLE)
    payment_sign = models.BooleanField(default=False, verbose_name='признак оплаты')
    payment_sum = models.CharField(max_length=100, verbose_name='сумма оплаты', **NULLABLE)
    payment_method = models.CharField(max_length=100, choices=PAY_METHOD, verbose_name='способ оплаты', **NULLABLE)
    payment_date = models.DateField(auto_now_add=True, verbose_name='дата оплаты', **NULLABLE)


    def __str__(self):
        return (f'{self.payment_sum}'
                f'{self.payment_method}'
                f'{self.payment_date}')

    class Meta:

        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
