from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import DirectionViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r'dir', DirectionViewSet, basename='direction')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='view'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete'),

] + router.urls
