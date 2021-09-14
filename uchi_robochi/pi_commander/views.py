from rest_framework import viewsets
from .serializers import UserSerializer, RaspberrySerializer
from django.contrib.auth.models import User
from .models import Raspberry

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RaspberryViewSet(viewsets.ModelViewSet):
    queryset = Raspberry.objects.all()
    serializer_class = RaspberrySerializer
