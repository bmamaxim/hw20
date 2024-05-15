from rest_framework import serializers

from materials.models import Direction, Lesson


class DirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direction
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
