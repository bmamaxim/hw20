from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Direction, Lesson
from materials.serializers import DirectionSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner


class DirectionViewSet(viewsets.ModelViewSet):
    """
    View set diretion clsases
    """
    serializer_class = DirectionSerializer
    queryset = Direction.objects.all()

    def perform_create(self, serializer):
        direction = serializer.save()
        direction.owner = self.request.user
        direction.save()


    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModerator,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModerator | IsOwner)
        elif self.action == "destroy":
            self.permission_classes = (~IsModerator, IsOwner)
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator,)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()



class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()



class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | ~IsModerator]
