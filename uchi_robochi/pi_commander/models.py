from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

TIME_UNIT_OPTIONS = [("D", "Days"), ("H", "Hours"), ("M", "Minutes"), ("S", "Seconds")]


class Raspberry(models.Model):
    name = models.CharField(max_length=100, default="Raspberry 1")
    ip_address = models.GenericIPAddressField()
    owner = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Relay(models.Model):
    label = models.CharField(max_length=40, default="Relay 1")
    raspberry = models.ForeignKey(Raspberry, on_delete=CASCADE)

    def __str__(self):
        return f"{self.label}"


class Action(models.Model):
    description = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=CASCADE)
    raspberry = models.ForeignKey(Raspberry, on_delete=CASCADE)
    relay = models.ForeignKey(Relay, on_delete=CASCADE)
    status = models.BooleanField(default=False)
    time_out = models.IntegerField(blank=True, null=True)
    time_unit = models.CharField(max_length=1, choices=TIME_UNIT_OPTIONS, default="M")
    start_time = models.DateTimeField(default=None, blank=True, null=True)
    end_time = models.DateTimeField(default=None, blank=True, null=True)
