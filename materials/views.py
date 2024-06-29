from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from materials.models import Direction, Lesson, Subscription
from materials.paginators import MaterialsPaginator
from materials.serializers import (
    DirectionSerializer,
    LessonSerializer,
    SubscriptionSerializer,
)
from users.permissions import IsModerator, IsOwner
from users.tasks import send_direction_create, send_telegram_message


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="description from swagger_auto_schema via method_decorator"
    ),
)
class DirectionViewSet(viewsets.ModelViewSet):
    """
    View set diretion clsases
    """

    serializer_class = DirectionSerializer
    queryset = Direction.objects.all()
    pagination_class = MaterialsPaginator

    def perform_create(self, serializer):
        """
        Привязка курса к создателю
        :param serializer:
        :return:
        """
        direction = serializer.save()
        direction.owner = self.request.user
        direction.save()

    def get_permissions(self):
        """
        Раздаем допуск к действиям
        :return:
        """
        if self.action == "create":
            self.permission_classes = (~IsModerator,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = IsModerator | IsOwner
        elif self.action == "destroy":
            self.permission_classes = (~IsModerator, IsOwner)
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Регистрируем урок.
    """

    serializer_class = LessonSerializer
    permission_classes = (~IsModerator,)

    def perform_create(self, serializer):
        """
        Привязка урока к пользователю.
        :param serializer:
        :return:
        """
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """
    Просмотр всх уроков.
    """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MaterialsPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр подробностей по уроку.
    """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Изменить урок.
    """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Удалить урок.
    """

    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | ~IsModerator]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """
    Создать подписку
    """

    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        """
        Функция создания и удаления подписки
        вывод сообщения о действии
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user = self.request.user
        course_id = self.request.data.get("direction")

        course_item = get_object_or_404(Direction, pk=course_id)

        if Subscription.objects.filter(user=user, direction=course_item).exists():
            Subscription.objects.get(user=user, direction=course_item).delete()
            message = "подписка удалена"
            send_direction_create.delay(user.email, message)
            send_telegram_message(user.tg_id, message)
        else:
            Subscription.objects.create(user=user, direction=course_item)
            message = "подписка добавлена"
            send_direction_create.delay(user.email, message)
            send_telegram_message(user.tg_id, message)

        return Response({"message": message})
