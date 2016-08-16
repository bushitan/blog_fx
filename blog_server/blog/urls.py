# -*- coding: utf-8 -*-

from django.conf.urls import url
from blog.views import *
urlpatterns = [

   url(r'^index/$', IndexView.as_view()),
   # url(r'^gallery/(?P<open_id>\w+)$', GalleryView.as_view()),

   url(r'^gallery/$', GalleryView.as_view()),

   url(r'^artwork/$', ArtworkAddView.as_view()),
   url(r'^artwork/show/$', ArtworkShowView.as_view()),

   url(r'^game/(?P<game_id>\w+)$', GameView.as_view()),
   url(r'^game/add/$', GameAddView.as_view()),
]