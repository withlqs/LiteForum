from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from user.models import User
from .forms import TopicForm
from .models import Topic, Node


def home(request):
    # raw_tlist = Topic.objects.all()
    raw_nlist = Node.objects.all()

    # tl = []
    # for t in raw_tlist:
    #     tl.append((t, t.upd_date))

    tn = []
    for n in raw_nlist:
        tn.append((n, n.topic_set.count()))

    # tlist = [x for x, y in sorted(tl, key=lambda x:x[1])[:20]]
    tlist = Topic.objects.order_by('-pub_date')
    nlist = sorted(tn, key=lambda x: -x[1])[:10]

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
    nlist = Node.objects.all()
    return render(request, 'topic/node_list.html', {'nlist': nlist})


def new_post(requset):
    if requset.method == 'POST':
        form = TopicForm(requset.POST)
        if form.is_valid():
            t = Topic()
            t.title = form.cleaned_data['title']
            t.content = form.cleaned_data['content']
            t.node = form.cleaned_data['node']
            t.author = User.objects.get(username=requset.user)
            # print(requset.user)
            t.pub_date = timezone.now()
            t.upd_date = timezone.now()
            t.save()
            return HttpResponseRedirect('/')
    else:
        form = TopicForm()
    return render(requset, 'topic/new_post.html', {'form': form})


def test(request):
    return render(request, 'test.html', {})
