# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20151001_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('my_order',)},
        ),
        migrations.AddField(
            model_name='article',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
