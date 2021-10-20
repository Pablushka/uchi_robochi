from django.db.models import query
from rest_framework import viewsets
from .serializers import RelaySerializer, UserSerializer, RaspberrySerializer, ActionSerializer
from django.contrib.auth.models import User
from .models import Raspberry
from .models import Relay, Action

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RaspberryViewSet(viewsets.ModelViewSet):
    queryset = Raspberry.objects.all()
    serializer_class = RaspberrySerializer

class RelayViewSet (viewsets.ModelViewSet):
    queryset = Relay.objects.all()
    serializer_class = RelaySerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
