# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='parent_ID',
        ),
    ]
