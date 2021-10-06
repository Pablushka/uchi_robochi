from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Raspberry(models.Model):
    name = models.CharField(max_length=100, default="Raspberry 1")
    ip_address = models.GenericIPAddressField()
    owner = models.ForeignKey(User,on_delete=CASCADE)
    
    def __str__(self):
        return "{0}".format(self.name)

class Relay(models.Model):
    name= models.CharField(max_length=40, default="Relay 1")
    raspberry= models.ForeignKey(Raspberry,on_delete= CASCADE)
    label = models.CharField(max_length=12 , default="Switch 1")
    description=models.CharField(max_length=250, default= "" )