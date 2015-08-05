# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20150721_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='parent_ID',
        ),
        migrations.AddField(
            model_name='article',
            name='parent',
            field=models.ForeignKey(default=0, to='articles.Article'),
            preserve_default=False,
        ),
    ]
