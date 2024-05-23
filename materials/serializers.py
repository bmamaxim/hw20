from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Direction, Lesson, Subscription
from materials.vatidators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'title_lesson', 'description_lesson', 'owner', 'url_lesson')
        validators = [UrlValidator(field='url_lesson')]


class DirectionSerializer(serializers.ModelSerializer):
    lesson = SerializerMethodField()

    def get_lesson(self, direction):
        return Lesson.objects.filter(direction=direction).count()

    def get_subscription(self, obj):
        request = self.context.get('request')
        user = None
        if request:
            user = request.user
        return obj.subscription_set.filter(user=user).exists()

    class Meta:
        model = Direction
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('user', 'direction')
