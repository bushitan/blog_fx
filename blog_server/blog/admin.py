# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('openid_wx',)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(User,UserAdmin)
admin.site.register(Gallery,GalleryAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Game,GameAdmin)