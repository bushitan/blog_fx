# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class string_with_title(str):
    """ 用来修改admin中显示的app名称,因为admin app 名称是用 str.title()显示的,
    所以修改str类的title方法就可以实现.
    """
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

class User(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=32, verbose_name=u'名称')
    openid_wx = models.CharField(max_length=32, verbose_name=u'微信OpenID')
    class Meta:
        verbose_name_plural = verbose_name = u'用户'
        app_label = string_with_title('blog', u"博客")
    def __unicode__(self):
        return '%s' % (self.openid_wx)

class Gallery(models.Model):
    user =  models.ForeignKey(User, verbose_name=u'画家')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    img_url =  models.CharField(max_length=200, verbose_name=u'原图地址')
    char_img_url = models.CharField(max_length=200, verbose_name=u'字符画地址')
    class Meta:
        verbose_name_plural = verbose_name = u'画廊'
        ordering = ['-create_time']
        app_label = string_with_title('blog', u"博客")
