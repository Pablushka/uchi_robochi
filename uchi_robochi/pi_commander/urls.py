from django.urls import path, include
from rest_framework import routers
from .views import RaspberryViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"raspberry", RaspberryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
