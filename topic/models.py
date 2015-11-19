from django.db import models

from user.models import User


class Node(models.Model):
    name = models.CharField(max_length=20, unique=True)
    codename = models.CharField(max_length=20, primary_key=True)


class Topic(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000, null=True)
    pub_date = models.DateTimeField(null=True)
    upd_date = models.DateTimeField(null=True)
    node = models.ForeignKey(Node, null=True)
    author = models.ForeignKey(User, null=True)
    reply_count = models.IntegerField(default=0)
    fav_count = models.IntegerField(default=0)


class Reply(models.Model):
    content = models.TextField(max_length=20000)
    reply_to = models.ForeignKey(Topic, null=True)
    author = models.ForeignKey(User, null=True)
    pub_date = models.DateTimeField(null=True)
