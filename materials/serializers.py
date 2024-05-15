from rest_framework.serializers import ModelSerializer

from materials.models import Direction, Lesson


class DirectionSerializer(ModelSerializer):

    class Meta:
        model = Direction
        fields = '__all__'


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
