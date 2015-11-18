from django.conf.urls import include, url
from django.contrib import admin

from topic.views import home, topic, node, node_list, new_post

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    # url(r'^member/(?P<username>[A-Za-z0-9]+)$', views.member, name='member'),
    url(r'^t/(?P<topic_id>\d+)/$', topic, name='topic'),
    url(r'^node/(?P<nodename>[A-Za-z0-9]+)$', node, name='node'),
    url(r'^nodes$', node_list, name='node_list'),
    # url(r'^settings$', views.settings, name='settings'),
    # url(r'^restore$', views.restore, name='restore'),
    # url(r'^logout$', views.logout, name='logout'),
    # url(r'^login$', views.login, name='login'),
    # url(r'^register$', views.register, name='register'),
    url(r'^new$', new_post, name='new_post'),
]
