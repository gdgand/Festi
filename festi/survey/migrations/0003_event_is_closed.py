# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20150406_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_closed',
            field=models.BooleanField(default=True, db_index=True),
            preserve_default=True,
        ),
    ]
