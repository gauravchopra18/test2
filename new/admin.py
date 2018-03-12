from django.contrib import admin
from .models import *


admin.site.register(connect)
admin.site.register(relation)


def pub(modelAdmin,request,queryset):
    queryset.update(
        privacy='public'
    )
pub.short_description='set privacy as public'


def priv(modelAdmin,request,queryset):
    queryset.update(
        privacy='private'
    )
priv.short_description='set privacy as private'


def frnd(modelAdmin,request,queryset):
    queryset.update(
        privacy='friends'
    )
frnd.short_description='set privacy as friends'


class adminPost(admin.ModelAdmin):
   list_display = ['post','privacy','user',]
   list_editable = ['privacy',]
   list_filter = ['privacy','user']
   search_fields = ['post']
   date_hierarchy = 'date'
   actions = [priv,pub,frnd]
admin.site.register(Post,adminPost)