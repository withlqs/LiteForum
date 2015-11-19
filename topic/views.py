from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import TopicForm
from .models import Topic, Node


def home(request):
    tlist = Topic.objects.order_by('-reply_count')
    nlist = Node.objects.all()
    return render(request, 'topic/home.html', {'tlist': tlist, 'nlist': nlist})


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
    if requset.method == 'GET':
        form = TopicForm()
        return render(requset, 'topic/new_post.html', {'form': form})
    return HttpResponse("New Post")


def test(request):
    return render(request, 'test.html', {})
