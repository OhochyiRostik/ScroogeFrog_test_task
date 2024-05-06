from django.db import models
from users.models import User


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizer_event')
    visitor = models.ManyToManyField(User, through='Registration', related_name='visitor_event')

    def __str__(self):
        return self.name


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.email} - {self.event.name}'
