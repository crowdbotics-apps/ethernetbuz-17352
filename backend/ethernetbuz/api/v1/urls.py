from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EthernetbuzViewSet

router = DefaultRouter()
router.register("ethernetbuz", EthernetbuzViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
