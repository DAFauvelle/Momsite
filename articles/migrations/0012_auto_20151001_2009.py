# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_imagepdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='parent',
            field=models.ForeignKey(blank=True, to='articles.Article', null=True),
            preserve_default=True,
        ),
    ]
