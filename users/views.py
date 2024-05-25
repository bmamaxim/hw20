from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from users.models import Payment, User
from users.serializers import UserSerializer, PaymentSerializer
from users.services import convert_rub_to_usd, create_stripe_price, create_stripe_session


class PaymentListAPIView(generics.ListAPIView):
    """
    Просмотр всех оплат.
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'payment_method')
    ordering_fields = ('payment_date',)


class PaymentCreateAPIView(generics.CreateAPIView):
    """
    Создаем оплату курса через stripe.
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        # для использования конвертации convert_rub_to_usd: users -> services
        # amount_in_dollars = convert_rub_to_usd(payment.amount)
        price = create_stripe_price(payment.amount)
        session_id, payment_link = create_stripe_session(price)
        payment.payment_id = session_id
        payment.link = payment_link
        payment.save()


class UserListAPIView(generics.ListAPIView):
    """
    Просмотр всех юзеров.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    """
    Регистрация.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Вход - Login.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Изминение пользователя.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление пользователя.
    """
    queryset = User.objects.all()
