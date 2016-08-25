# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160806_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': '\u6e38\u620f\u6570\u636e', 'verbose_name_plural': '\u6e38\u620f\u6570\u636e'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='sketch_url',
            field=models.CharField(max_length=200, null=True, verbose_name='\u5b57\u7b26\u753b\u5730\u5740'),
        ),
    ]
