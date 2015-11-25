from django.contrib import admin

from .models import *


class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 1


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    inlines = [ReplyInline]


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'pub_date')
    inlines = [ReplyInline]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply)
admin.site.register(Node)
admin.site.register(User)
