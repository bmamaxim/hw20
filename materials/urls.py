from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import DirectionViewSet, LessonCreateAPIView

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r'dir', DirectionViewSet, basename='direction')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='create'),
] + router.urls
