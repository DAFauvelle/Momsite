# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20150807_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='la_photo',
            field=models.ImageField(max_length=255, upload_to=b'/static/media/images/'),
            preserve_default=True,
        ),
    ]
