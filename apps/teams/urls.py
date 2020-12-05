from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.teams.views import TeamsViewSet


router = DefaultRouter()
router.register(r'^teams', TeamsViewSet, basename='teams')

urlpatterns = [
    url('', include(router.urls)),
]
