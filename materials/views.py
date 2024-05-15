from django.shortcuts import render
from rest_framework import viewsets

from materials.models import Direction, Lesson
from materials.serializers import DirectionSerializer, LessonSerializer


class DirectionViewSet(viewsets.ModelViewSet):

    serializer_class = DirectionSerializer
    queryset = Direction.objects.all


class LessonViewSet(viewsets.ModelViewSet):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all
