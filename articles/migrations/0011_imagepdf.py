# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20150807_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePDF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('la_photo', models.FileField(max_length=255, upload_to=b'images/')),
                ('article', models.ForeignKey(to='articles.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
