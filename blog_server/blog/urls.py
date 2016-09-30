# -*- coding: utf-8 -*-

from django.conf.urls import url
from blog.views import *

urlpatterns = [

   url(r'^index/$', IndexView.as_view()),
   # url(r'^gallery/(?P<open_id>\w+)$', GalleryView.as_view()),

   url(r'^gallery/$', GalleryView.as_view()),

   url(r'^artwork/$', ArtworkAddView.as_view()), # 增加数据
   url(r'^artwork/show/$', ArtworkShowView.as_view()), #普通模式
   url(r'^artwork/hard/$', ArtworkHardView.as_view()), #高阶模式

   url(r'^game/(?P<game_id>\w+)$', GameView.as_view()),
   url(r'^game/add/$', GameAddView.as_view()),


   url(r'^board/$', BoardView.as_view()),
   url(r'^wx/$', WXView.as_view()),
]