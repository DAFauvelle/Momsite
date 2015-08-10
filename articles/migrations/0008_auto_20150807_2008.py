# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='la_photo',
            field=models.ImageField(max_length=255, upload_to=b'/static/media/'),
            preserve_default=True,
        ),
    ]
