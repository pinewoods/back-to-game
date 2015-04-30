from django.db import models

# Create your models here.

class GenericContent(models.Model):
    dummy = models.CharField(max_length=128)

class Student(models.Model):
    contents = models.ManytoManyField(GenericContent, through='SyncedContent')

class SyncedContent(models.Model):
    student = models.ForeignKey(Student)
    content = models.ForeignKey(GenericContent)
    is_synced = models.BooleanField(default=False)
    score = models.CharField(max_length=128)

