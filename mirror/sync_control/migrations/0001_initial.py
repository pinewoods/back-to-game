# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericContent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('dummy', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SyncedContent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_synced', models.BooleanField(default=False)),
                ('score', models.CharField(null=True, max_length=128)),
                ('content', models.ForeignKey(to='sync_control.GenericContent')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('SD', 'Student'), ('TC', 'Teacher')], max_length=2)),
                ('contents', models.ManyToManyField(to='sync_control.GenericContent', through='sync_control.SyncedContent')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='syncedcontent',
            name='user',
            field=models.ForeignKey(to='sync_control.UserProfile'),
        ),
    ]
