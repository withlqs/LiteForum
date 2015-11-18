from django.db import models


class User(models.Model):
    id = models.CharField(null=False, max_length=30, unique=True)
    email = models.EmailField(null=False, unique=True)
    site = models.TextField()
    location = models.TextField()
    comment = models.TextField()
