from django.db import models
from django.contrib.auth.models import User

from rest_framework import serializers


class GenericContent(models.Model):
    dummy = models.CharField(max_length=128)

    def __str__(self):
        return '<%s>' % (self.dummy,)


class UserProfile(models.Model):
    USER_ROLE_CHOICES = (
        ('SD', 'Student'),
        ('TC', 'Teacher'),
    )
    user = models.OneToOneField(User)
    role = models.CharField(max_length=2,
        choices=USER_ROLE_CHOICES)
    contents = models.ManyToManyField(GenericContent,
            through='SyncedContent')

    def __str__(self):
        return '<%s>' % (self.user.username,)


class SyncedContent(models.Model):
    user = models.ForeignKey(UserProfile)
    content = models.ForeignKey(GenericContent)
    is_synced = models.BooleanField(default=False)
    score = models.CharField(max_length=128,
            blank=True) # TODO FK

    def __str__(self):
        return '<%s - %s>' % (self.user.user.username, self.content.dummy)


class SyncedContentSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    content = serializers.IntegerField()
    is_synced = serializers.BooleanField()
