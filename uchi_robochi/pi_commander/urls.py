from django.urls import path, include
from rest_framework import routers
from .views import ActionViewSet, RaspberryViewSet, UserViewSet, RelayViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"raspberry", RaspberryViewSet)
router.register(r"relay",RelayViewSet)
router.register(r"action",ActionViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
