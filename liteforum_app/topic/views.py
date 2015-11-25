from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from liteforum_app.user.models import User
from .forms import TopicForm, ReplyForm
from .models import Topic, Node, Reply


def logged(request):
    return HttpResponseRedirect('/')


def home(request):
    raw_nlist = Node.objects.all()
    tn = []
    for n in raw_nlist:
        tn.append((n, n.topic_set.count()))
    tlist = Topic.objects.order_by('-upd_date')
    tlist = [(t, t.author.get_user()['gravatar']) for t in tlist]
    nlist = sorted(tn, key=lambda x: -x[1])[:10]
    # print(nlist)

    xuser = ''
    if request.user.is_authenticated() \
            and User.objects.filter(username=request.user.username) is not None \
            and request.user.username != 'admin':
        xuser = User.objects.get(username=request.user.get_username()).get_user()

    return render(request, 'home.html', {'tlist': tlist, 'nlist': nlist, 'user': xuser})


def member(request, username):
    return HttpResponse("Member Page: %s" % username)


def topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    raw_rlist = topic.reply_set.order_by('pub_date')
    rid = 0
    rlist = []
    user = topic.author.get_user()
    for r in raw_rlist:
        rid += 1
        rlist.append((rid, r, r.author.get_user()['gravatar']))
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if (form.is_valid()):
            r = Reply()
            r.content = form.cleaned_data['content']
            r.author = User.objects.get(username=request.user)
            r.pub_date = timezone.now()
            r.reply_to = topic
            topic.upd_date = timezone.now()
            r.save()
            topic.save()
            return HttpResponseRedirect("#")
    else:
        form = ReplyForm()

    return render(request, 'topic_detail.html', {'t': topic, 'rlist': rlist, 'form': form, 'user': user})


def node(request, nodename):
    node = get_object_or_404(Node, codename=nodename)
    tlist = node.topic_set.order_by('-upd_date')
    tlist = [(t, t.author.get_user()['gravatar']) for t in tlist]

    raw_nlist = Node.objects.all()
    tn = []
    for n in raw_nlist:
        tn.append((n, n.topic_set.count()))
    nlist = sorted(tn, key=lambda x: -x[1])[:10]
    return render(request, 'node.html', {'node': node, 'tlist': tlist, 'nlist': nlist})


def node_list(request):
    nlist = Node.objects.all()
    return render(request, 'node_list.html', {'nlist': nlist})


def new_post(requset):
    if requset.method == 'POST':
        form = TopicForm(requset.POST)
        if form.is_valid():
            t = Topic()
            t.title = form.cleaned_data['title']
            t.content = form.cleaned_data['content']
            t.node = form.cleaned_data['node']
            t.author = User.objects.get(username=requset.user)  # 这里可能出问题, 应该判断是否找不到对象
            # print(requset.user)
            t.pub_date = timezone.now()
            t.upd_date = timezone.now()
            t.save()
            return HttpResponseRedirect('/t/%s' % t.id)
    else:
        form = TopicForm()
    return render(requset, 'new_post.html', {'form': form})


def test(request):
    return render(request, 'test.html', {})
