# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20150806_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('la_photo', models.ImageField(max_length=255, upload_to=b'')),
                ('article', models.ForeignKey(to='articles.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
