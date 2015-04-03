# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20150322_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='approve_email_content',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
