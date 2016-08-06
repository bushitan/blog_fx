# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('circle', models.TextField(verbose_name='\u5706\u5708\u4f4d\u7f6e')),
                ('color', models.TextField(verbose_name='\u989c\u8272')),
                ('img_url', models.TextField(verbose_name='\u539f\u56feurl')),
                ('str_url', models.TextField(verbose_name='\u5b57\u7b26\u753burl')),
                ('stage', models.TextField(verbose_name='\u821e\u53f0')),
            ],
            options={
                'verbose_name': '\u6e38\u620f',
                'verbose_name_plural': '\u6e38\u620f',
            },
        ),
        migrations.AlterField(
            model_name='gallery',
            name='user',
            field=models.ForeignKey(verbose_name='\u753b\u5bb6', to='blog.User'),
        ),
    ]
