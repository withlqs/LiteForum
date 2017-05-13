from django.conf.urls import url

from .topic.views import home, topic, node, node_list, new_post
from .user.views import login, logged, logout, profile, profile_edit, restore, register

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^t/(?P<topic_id>\d+)$', topic, name='topic'),
    url(r'^nodes/(?P<nodename>[A-Za-z0-9]+)$', node, name='node'),
    url(r'^nodes$', node_list, name='node_list'),
    url(r'^new$', new_post, name='new_post'),

    url(r'^accounts/login/+$', login),
    url(r'^accounts/logout/+$', logout),
    url(r'^accounts/register/+$', register),
    url(r'^accounts/profile/+$', logged),
    url(r'^accounts/profile/(?P<user_id>[0-9])/+$', profile),
    url(r'^accounts/profile/edit/+$', profile_edit),
    url(r'^accounts/restore/+$', restore),
]
