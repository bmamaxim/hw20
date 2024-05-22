from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Direction, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'title_lesson', 'description_lesson', 'owner')


class DirectionSerializer(serializers.ModelSerializer):
    lesson = SerializerMethodField()

    def get_lesson(self, direction):
        return Lesson.objects.filter(direction=direction).count()

    class Meta:
        model = Direction
        fields = '__all__'
