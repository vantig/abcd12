from django.db import models
from django.conf import settings


class Task(models.Model):
    title = models.CharField(max_length=30)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
