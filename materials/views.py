from django.shortcuts import render
from rest_framework import viewsets, generics

from materials.models import Direction, Lesson
from materials.serializers import DirectionSerializer, LessonSerializer


class DirectionViewSet(viewsets.ModelViewSet):

    serializer_class = DirectionSerializer
    queryset = Direction.objects.all


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
