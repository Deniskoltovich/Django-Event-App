from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    event_creator = models.ForeignKey(User, related_name = 'event_creator', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=False)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=256, blank=False)
    attendees = models.ManyToManyField(User, related_name = 'attendees' )