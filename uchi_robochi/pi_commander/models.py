from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Raspberry(models.Model):
    name = models.CharField(max_length=100, default="Raspberry 1")
    ip_address = models.GenericIPAddressField()
    owner = models.ForeignKey(User,on_delete=CASCADE)
    
