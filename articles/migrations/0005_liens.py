# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('addresse', models.URLField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
