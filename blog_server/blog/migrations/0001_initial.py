# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('img_url', models.CharField(max_length=200, verbose_name='\u539f\u56fe\u5730\u5740')),
                ('char_img_url', models.CharField(max_length=200, verbose_name='\u5b57\u7b26\u753b\u5730\u5740')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u753b\u5eca',
                'verbose_name_plural': '\u753b\u5eca',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField()),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u79f0')),
                ('openid_wx', models.CharField(max_length=32, verbose_name='\u5fae\u4fe1OpenID')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='user',
            field=models.ForeignKey(verbose_name='\u6545\u4e8b', to='blog.User'),
        ),
    ]
