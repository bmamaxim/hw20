import django_filters
from rest_framework import serializers

from materials.models import Direction, Lesson
from users.models import Payment


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title_lesson', 'description_lesson')


class DirectionSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Direction
        fields = '__all__'



