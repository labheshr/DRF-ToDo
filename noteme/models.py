from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    done = models.BooleanField(default=False)
