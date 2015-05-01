from django.db import models
from rest_framework import serializers

class GenericContent(models.Model):
    dummy = models.CharField(max_length=128)

class Student(models.Model):
    contents = models.ManyToManyField(GenericContent,
            through='SyncedContent')

class SyncedContent(models.Model):
    student = models.ForeignKey(Student)
    content = models.ForeignKey(GenericContent)
    is_synced = models.BooleanField(default=False)
    score = models.CharField(max_length=128) # TODO FK

class SyncedContentSerializer(serializers.Serializer):
    student = serializers.EmailField()
    content = serializers.IntegerField()
    is_synced = serializers.BooleanField()

