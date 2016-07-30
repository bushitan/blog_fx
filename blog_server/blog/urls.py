# -*- coding: utf-8 -*-

from django.conf.urls import url
from blog.views import *
urlpatterns = [

   url(r'^index/$', IndexView.as_view()),
   url(r'^gallery/(?P<open_id>\w+)$', GalleryView.as_view()),

   url(r'^artwork/$', ArtworkView.as_view()),

]