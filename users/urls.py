from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView, PaymentListAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('', UserListAPIView.as_view(), name='users'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-view'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
    # Payment
    path('pay/', PaymentListAPIView.as_view(), name='pay'),
]
