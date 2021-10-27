import factory
from pi_commander import models
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    username = 'Jorge'


class RaspberryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Raspberry

    name = 'Pepe'
    ip_address = '10.24.33.19'
    owner = factory.SubFactory(UserFactory)

