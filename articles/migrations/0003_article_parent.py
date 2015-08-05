# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_parent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='parent',
            field=models.ForeignKey(default='0', to='articles.Article'),
            preserve_default=False,
        ),
    ]
