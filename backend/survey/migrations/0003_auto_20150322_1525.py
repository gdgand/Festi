# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20150322_1447'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('auth_type', 'uid')]),
        ),
    ]
