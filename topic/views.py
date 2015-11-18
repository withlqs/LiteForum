from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Topic


def home(request):
    return HttpResponse("Home Page")


def member(request, username):
    return HttpResponse("Member Page: %s" % username)


def topic_list(request):
    return HttpResponse("Topic List Page")


def topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    replies = topic.reply_set.all()
    return render(request, 'topic/topic.html', {'topic': topic, 'replies': replies})


def node(request, nodename):
    return HttpResponse("Node name: %s" % nodename)


def node_list(request):
    return HttpResponse("Nodes page")


def new_post(requset):
    return HttpResponse("New Post")
