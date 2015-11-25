from liteforum_app.topic import Topic, Reply


def user_topic_history(username):
    return Topic.objects.filter(author__username=username).order_by('-pub_date')


def user_reply_history(username):
    return Reply.objects.filter(author__username=username).order_by('-pub_date')
