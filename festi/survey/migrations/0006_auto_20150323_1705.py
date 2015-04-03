# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20150323_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='is_attended',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\ucc38\uc11d\uc5ec\ubd80'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='survey',
            name='is_approved',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\uc2b9\uc778\uc5ec\ubd80'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='survey',
            name='is_notified',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\uc54c\ub9bc\uc5ec\ubd80'),
            preserve_default=True,
        ),
    ]
