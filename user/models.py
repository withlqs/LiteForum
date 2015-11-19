from django.db import models


class User(models.Model):
    username = models.CharField(null=False, max_length=30, unique=True)
    email = models.EmailField(null=False, unique=True)
    site = models.TextField(default='')
    location = models.TextField(default='')
    comment = models.TextField(default='')
