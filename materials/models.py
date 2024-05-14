from django.db import models

from users.models import NULLABLE


class Direction(models.Model):

    title_direction = models.CharField(max_length=200, verbose_name='направление', **NULLABLE)
    preview_direction = models.ImageField(upload_to='image/', verbose_name='герб', **NULLABLE)
    description_direction = models.CharField(max_length=1000, verbose_name='описание направления', **NULLABLE)

    def __str__(self):
        return (f'{self.title_direction}'
                f'{self.description_direction}')

    class Meta:

        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):

    direction = models.ManyToManyField(Direction, on_delete=models.SET_NULL, verbose_name='курс')
    title_lesson = models.CharField(max_length=200, verbose_name='название урока', **NULLABLE)
    description_lesson = models.CharField(max_length=1000, verbose_name='описание урока', **NULLABLE)
    preview_lesson = models.ImageField(upload_to='image/', verbose_name='значек', **NULLABLE)
    url_lesson = models.CharField(max_length=150, verbose_name='ссылка на урок', **NULLABLE)


    def __str__(self):
        return (f'{self.title_lesson}'
                f'{self.description_lesson}'
                f'{self.direction}')

    class Meta:

        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
