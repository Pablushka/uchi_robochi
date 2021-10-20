from .models import Raspberry, Relay, Action
from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
        fields = ["id", "label", "raspberry", "description"]

    def validate(self, data):   
        """
        creates rules for avoiding same relay name for one raspberry
        """
        result = Relay.objects.filter(label = data["label"], raspberry = data["raspberry"])
        if result :
            raise ValidationError(
                _('%(label)s is taken for %(raspberry)s'), 
                params={'label': data["label"], 'raspberry': data["raspberry"] },
            )
        return data

class ActionSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "description", "user", "raspberry", "relay", "status"]

    def validate(self, data):
        """
        rule to validate that action description is unique for same user, raspberry and relay
        """
        result = Action.objects.filter(description = data["description"], user = data["user"], raspberry = data["raspberry"], relay = data["relay"])
        if result :
            raise ValidationError(
                _('%(description)s is already in use for this %(relay)s in raspberry %(raspberry)s'),
                params = {'description': data["description"], 'user': data["user"], 'raspberry': data["raspberry"]},
            )
        return data