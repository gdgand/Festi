# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import conference.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idx', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(upload_to=conference.models.random_name)),
                ('topic', models.CharField(max_length=100, blank=True)),
                ('detail', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('idx', 'id'),
            },
            bases=(models.Model,),
        ),
    ]
