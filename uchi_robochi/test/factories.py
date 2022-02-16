import factory
from pi_commander import models
from django.contrib.auth.models import User
from faker import Faker as f
import random

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    username = f().name()
 
 
class RaspberryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Raspberry

    name = f().domain_word()
    ip_address = '10.24.33.19'
    owner = factory.SubFactory(UserFactory)

