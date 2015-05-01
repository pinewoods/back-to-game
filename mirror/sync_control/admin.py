from django.contrib import admin

# Register your models here.
from django.contrib import admin
from sync_control.models import GenericContent
from sync_control.models import Student
from sync_control.models import SyncedContent

admin.site.register(GenericContent)
admin.site.register(Student)
admin.site.register(SyncedContent)
