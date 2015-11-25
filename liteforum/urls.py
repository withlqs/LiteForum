import user
from django.conf.urls import include, url
from django.contrib import admin

from liteforum_app.topic import home, topic, node, node_list, new_post, test

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^t/(?P<topic_id>\d+)$', topic, name='topic'),
    url(r'^nodes/(?P<nodename>[A-Za-z0-9]+)$', node, name='node'),
    url(r'^nodes$', node_list, name='node_list'),
    url(r'^new$', new_post, name='new_post'),

    url(r'^accounts/login/+$', liteforum_app.user.views.login),
    url(r'^accounts/logout/+$', liteforum_app.user.views.logout),
    url(r'^accounts/register/+$', liteforum_app.user.views.register),
    url(r'^accounts/profile/+$', liteforum_app.user.views.logged),
    url(r'^accounts/profile/(?P<user_id>[0-9])/+$', liteforum_app.user.views.profile),
    url(r'^accounts/profile/edit/+$', liteforum_app.user.views.profile_edit),
    url(r'^accounts/restore/+$', liteforum_app.user.views.restore),
    url(r'^test$', test)
]
