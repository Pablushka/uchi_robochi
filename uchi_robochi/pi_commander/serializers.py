from .models import Raspberry
from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Relay


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "password", "is_staff"]


class RaspberrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Raspberry
        fields = ["id", "name", "ip_address", "owner"]

    def validate(self, data):    
        """creates rules for avoiding same raspberry name for one owner"""
        result = Raspberry.objects.filter(name = data["name"], owner = data["owner"])
        if result :
            raise ValidationError(
                _('%(name)s is taken for %(owner)s'), 
                params={'name': data["name"], 'owner': data["owner"] },
            )
        return data

class RelaySerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relay
        fields = ["id","name","raspberry","label","description"]