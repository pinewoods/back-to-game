from django.db import models
from django.contrib.auth.models import User

from rest_framework import serializers


class GenericContent(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField(blank=True)

    def __str__(self):
        return '<%s>' % (self.dummy,)


class GenericContentSerializer(serializers.Serializer):
    title = serializers.StringRelatedField()
    url = serializers.StringRelatedField()


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


class UserProfileSerializer(serializers.Serializer):
    user = serializers.StringRelatedField()
    contents = serializers.PrimaryKeyRelatedField(
            many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = ('user', 'role', 'contents')


class SyncedContent(models.Model):
    user = models.ForeignKey(UserProfile)
    content = models.ForeignKey(GenericContent)
    is_synced = models.BooleanField(default=False)
    score = models.CharField(max_length=128,
            blank=True) # TODO FK

    def __str__(self):
        return '<%s - %s>' % (self.user.user.username, self.content.dummy)

