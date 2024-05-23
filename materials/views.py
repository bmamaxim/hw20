from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from materials.models import Direction, Lesson, Subscription
from materials.paginators import MaterialsPaginator
from materials.serializers import DirectionSerializer, LessonSerializer, SubscriptionSerializer
from users.permissions import IsModerator, IsOwner


class DirectionViewSet(viewsets.ModelViewSet):
    """
    View set diretion clsases
    """
    serializer_class = DirectionSerializer
    queryset = Direction.objects.all()
    #pagination_class = MaterialsPaginator

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
    pagination_class = MaterialsPaginator


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


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('direction')

        course_item = get_object_or_404(Direction, pk=course_id)

        if Subscription.objects.filter(user=user, direction=course_item).exists():
            Subscription.objects.get(user=user, direction=course_item).delete()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user=user, direction=course_item)
            message = 'подписка добавлена'

        return Response({"message": message})
