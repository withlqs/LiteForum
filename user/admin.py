from django.contrib import admin

from topic.models import Topic, Reply, Node
from user.models import User


class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 1


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    inlines = [ReplyInline]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply)
admin.site.register(Node)
admin.site.register(User)
