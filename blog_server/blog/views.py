#coding:utf-8
from django.http import HttpResponse, Http404
from blog.models import *

from django.views.generic import  ListView
from models import *
import time
import json
import logging
import os
import base64

import sys

# logger
logger = logging.getLogger(__name__)


class BaseMixin(object):
    def get_context_data(self, *args, **kwargs):

        # user = self.request.user
        # if not user.is_authenticated():
        #    kwargs['user_id'] = "none"
        # else:
        #    kwargs['user_id'] = user
        context = super(BaseMixin, self).get_context_data(**kwargs)
        return context

class IndexView(BaseMixin, ListView):
    template_name = 'blog/index.html'
    # context_object_name = 'article_list'

    def get_context_data(self, **kwargs):
        pass
        # 轮播
        # kwargs['carousel_page_list'] = Carousel.objects.all()
        return super(IndexView, self).get_context_data(**kwargs)

    def get_queryset(self):
        # article_list = Article.objects.filter(status=0)
        # return article_list
         pass

#作品展示
class GalleryView(BaseMixin, ListView):
    template_name = 'blog/gallery.html'
    # context_object_name = 'article_list'
    open_id = ''
    def get_context_data(self, **kwargs):
        #查open_id 下，所有的图片做展示
        # _open_id = self.kwargs.get('open_id', '')
        _open_id = self.open_id
        if User.objects.filter(openid_wx = _open_id).exists():
            # print 1
            user = User.objects.get(openid_wx = _open_id)
            # print user
            kwargs['gallery'] = Gallery.objects.filter(user = user)
            kwargs['gallery_artwork_count'] = Gallery.objects.filter(user = user).count()
            kwargs['gallery_artwork_increase'] = 3

            # print kwargs['gallery']
            # print 'count:',kwargs['gallery_artwork_count']

        return super(GalleryView, self).get_context_data(**kwargs)
    def get_queryset(self):
        pass
    def get(self, request, *args, **kwargs):
        self.open_id = request.GET.get('open_id')

        return super(GalleryView, self).get(request, *args, **kwargs)


#增加新作品
class ArtworkAddView(BaseMixin, ListView):
    def get_context_data(self, **kwargs):
        # pass
        return super(ArtworkAddView, self).get_context_data(**kwargs)
    def get_queryset(self):
        pass
    def post(self, request, *args, **kwargs):
        _open_id = self.request.POST.get('open_id', '')
        _img_url = self.request.POST.get('img_url', '')
        _char_img_url = self.request.POST.get('char_img_url', '')
        _sketch_url = self.request.POST.get('sketch_url', '')


        #查 open_id 是否存在
        user = None
        if User.objects.filter(openid_wx = _open_id).exists() is False:
            #增加open_id
            user = User(
                uid = 11,
                name = '丰兄',
                openid_wx = _open_id
            )
            user.save()
        else:
            user = User.objects.get(openid_wx = _open_id)

        #增加新的作品
        g = Gallery(
            user = user,
            img_url = _img_url,
            char_img_url = _char_img_url,
            sketch_url = _sketch_url
        )
        g.save()

        mydict = {'state':1}
        return HttpResponse(
            json.dumps(mydict),
            content_type="application/json"
        )


        #添加2条url
        # pass

class ArtworkShowView(BaseMixin, ListView):
    template_name = 'blog/show.html'
    str_img = ''
    origin_img = ''
    sketch_img = ''
    open_id = ''
    def get_context_data(self, **kwargs):
        kwargs['str_img'] = self.str_img
        kwargs['origin_img'] = self.origin_img
        kwargs['sketch_img'] = self.sketch_img

        kwargs['open_id'] = self.open_id

        # print kwargs['url']
        return super(ArtworkShowView, self).get_context_data(**kwargs)
    def get_queryset(self):
        pass
    def get(self, request, *args, **kwargs):
        self.str_img = request.GET.get('str_img')
        self.origin_img = request.GET.get('origin_img')
        self.sketch_img = request.GET.get('sketch_img')
        self.open_id = request.GET.get('open_id')

        return super(ArtworkShowView, self).get(request, *args, **kwargs)

import httplib, urllib,urllib2
#小游戏
class GameView(BaseMixin, ListView):
    template_name = 'game/canvas_circle_event.html'
    # context_object_name = 'article_list'

    def get_context_data(self, **kwargs):
        #查open_id 下，所有的图片做展示
        _game_id = self.kwargs.get('game_id', '')
        print _game_id,'ok'
        if Game.objects.filter(id = _game_id).exists():
            kwargs['game_id'] = _game_id
        return super(GameView, self).get_context_data(**kwargs)
    def get_queryset(self):
        pass
    def get(self, request, *args, **kwargs):
        return super(GameView, self).get(request, *args, **kwargs)

    #跟数据库拿数据
    def post(self, request, *args, **kwargs):
        _game_id = self.request.POST.get('game_id', '')
        # if Game.objects.get(id = 2).exists() :
        g = Game.objects.get(id = _game_id)
        # print g.circle
        dict = {
            # 'circle' : g.circle,
            # 'color' : g.color,
            # 'img_url' : g.img_url,
            # 'str_url' : g.str_url,
            'stage' : g.stage
        }
        # print str(dict)
        return HttpResponse(
            json.dumps(dict),
            content_type="application/json"
        )
        # httpClient = None
        # try:
        #     url = 'http://127.0.0.1:8000/grid/api/game/'
        #     data  = {  "img_url":"http://127.0.0.1:8000/static/art/img/20160706154153.png"}
        #     req = urllib2.Request(url)
        #     data = urllib.urlencode(data)
        #     #enable cookie
        #     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        #     response = opener.open(req,data)
        #     res = response.read()
        #     # print res
        #     return HttpResponse(
        #         json.dumps(res),
        #         content_type="application/json"
        #     )
        #     # obj = json.loads(res)
        #     # print obj['img_url']
        #     # print obj['str_url']
        # except Exception, e:
        #     print e
        # finally:
        #     if httpClient:
        #         httpClient.close()


class GameAddView(BaseMixin, ListView):
    # template_name = 'game/canvas_circle_event.html'
    # context_object_name = 'article_list'
    def get_context_data(self, **kwargs):
        return super(GameAddView, self).get_context_data(**kwargs)
    def get_queryset(self):
        pass
    def post(self, request, *args, **kwargs):
        _circle = str(self.request.POST.get('circle', ''))
        _color = str(self.request.POST.get('color', ''))
        _img_url = str(self.request.POST.get('img_url', ''))
        _str_url = str(self.request.POST.get('str_url', ''))
        _stage = str(self.request.POST.get('stage', ''))


        _stage_data = str(self.request.POST.get('stage_data', ''))

        print _stage_data

        print _circle,_stage

        g = Game(
            # circle = _circle.encode('utf-8') ,
            # color = _color,
            # img_url = _img_url,
            # str_url = _str_url,
            # stage = _stage
            stage = _stage_data
        )
        g.save()

        return HttpResponse(
            json.dumps({'game_id':g.id}),
            content_type="application/json"
        )

