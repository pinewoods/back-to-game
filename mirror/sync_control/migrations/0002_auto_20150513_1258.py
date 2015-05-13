# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sync_control', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genericcontent',
            old_name='dummy',
            new_name='title',
        ),
        migrations.AddField(
            model_name='genericcontent',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='syncedcontent',
            name='score',
            field=models.CharField(default=0, blank=True, max_length=128),
            preserve_default=False,
        ),
    ]
