# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenericContent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('dummy', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SyncedContent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('is_synced', models.BooleanField(default=False)),
                ('score', models.CharField(max_length=128)),
                ('content', models.ForeignKey(to='sync_control.GenericContent')),
                ('student', models.ForeignKey(to='sync_control.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='contents',
            field=models.ManyToManyField(through='sync_control.SyncedContent', to='sync_control.GenericContent'),
        ),
    ]
