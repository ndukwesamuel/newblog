from django.contrib.auth.models import  User
from django.db import models

# Create your models here.


class Forum(models.Model):
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
