from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Direction(models.Model):

    title_direction = models.CharField(max_length=200, verbose_name='направление')
    preview_direction = models.ImageField(upload_to='image/', verbose_name='герб', **NULLABLE)
    description_direction = models.CharField(max_length=1000, verbose_name='описание направления', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)


    def __str__(self):
        return (f'{self.title_direction}'
                f'{self.description_direction}')


    class Meta:

        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):

    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, verbose_name='курс', **NULLABLE)
    title_lesson = models.CharField(max_length=200, verbose_name='название урока', **NULLABLE)
    description_lesson = models.CharField(max_length=1000, verbose_name='описание урока', **NULLABLE)
    preview_lesson = models.ImageField(upload_to='image/', verbose_name='значек', **NULLABLE)
    url_lesson = models.CharField(max_length=150, verbose_name='ссылка на урок', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)


    def __str__(self):
        return (f'{self.title_lesson}'
                f'{self.description_lesson}'
                f'{self.direction}')


    class Meta:

        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
