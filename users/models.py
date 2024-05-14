from django.contrib.auth.models import AbstractUser
from django.db import models

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


