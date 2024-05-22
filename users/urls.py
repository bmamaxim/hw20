from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView, PaymentListAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('', UserListAPIView.as_view(), name='users'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-view'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
    # Payment
    path('pay/', PaymentListAPIView.as_view(), name='pay'),
    # token
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
