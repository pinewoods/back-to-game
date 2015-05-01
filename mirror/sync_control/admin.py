from django.contrib import admin

# Register your models here.
from django.contrib import admin
from sync_control.models import GenericContent
from sync_control.models import UserProfile
from sync_control.models import SyncedContent

admin.site.register(GenericContent)
admin.site.register(UserProfile)
admin.site.register(SyncedContent)
