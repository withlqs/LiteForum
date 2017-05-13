from django.conf.urls import include, url
from django.contrib import admin

from liteforum_app.models import *

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Node)
admin.site.register(Reply)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('liteforum_app.urls'))
]
