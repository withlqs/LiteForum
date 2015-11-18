from django.db import models

from user.models import User


class Topic(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    pub_date = models.DateTimeField()
    upd_date = models.DateTimeField()
    node = models.ForeignKey(Node)
    author = models.ForeignKey(User)
    reply_count = models.IntegerField()
    fav_count = models.IntegerField()


class Reply(models.Model):
    content = models.TextField(max_length=20000)
    reply_to = models.ForeignKey(Topic)
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField()


class Node(models.Model):
    name = models.CharField(max_length=20, unique=True)
    codename = models.CharField(max_length=20, primary_key=True)
