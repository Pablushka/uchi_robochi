from .models import Raspberry
from django.contrib.auth.models import User
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "password", "is_staff"]


class RaspberrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Raspberry
        fields = ["id", "name", "ip_address", "owner"]
