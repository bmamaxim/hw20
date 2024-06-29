from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Direction, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name="элктронная почта")
    avatar = models.ImageField(
        upload_to="image/", verbose_name="изображение", **NULLABLE
    )
    phone = models.CharField(max_length=200, verbose_name="телефон", **NULLABLE)
    country = models.CharField(max_length=200, verbose_name="страна", **NULLABLE)
    tg_id = models.CharField(
        max_length=50, verbose_name="id telegramm", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.email} {self.phone} {self.country}"


class Payment(models.Model):
    PAY_CASH = "cash"
    PAY_NON_CASH = "non-cash"

    PAY_METHOD = (
        (PAY_CASH, "наличный"),
        (PAY_NON_CASH, "безнал"),
    )

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="студент", **NULLABLE
    )
    direction = models.ForeignKey(
        Direction, on_delete=models.SET_NULL, verbose_name="курс", **NULLABLE
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.SET_NULL, verbose_name="урок", **NULLABLE
    )
    payment_sign = models.BooleanField(default=False, verbose_name="признак оплаты")
    amount = models.PositiveIntegerField(
        help_text="сумма оплаты", verbose_name="сумма оплаты", **NULLABLE
    )
    payment_method = models.CharField(
        max_length=100, choices=PAY_METHOD, verbose_name="способ оплаты", **NULLABLE
    )
    payment_date = models.DateField(
        auto_now_add=True, verbose_name="дата оплаты", **NULLABLE
    )
    payment_id = models.CharField(
        max_length=300,
        verbose_name="id сессии оплаты",
        help_text="укажите id сессии",
        **NULLABLE,
    )
    link = models.URLField(
        max_length=400,
        verbose_name="ссылкак на оплату",
        help_text="ссылка на оплату",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.amount}" f"{self.payment_method}" f"{self.payment_date}"

    class Meta:

        verbose_name = "платеж"
        verbose_name_plural = "платежи"
