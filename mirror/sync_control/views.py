from django.shortcuts import render
from rest_framework import viewsets
from sync_control.models import SyncedContent
from sync_control.models import SyncedContentSerializer

class SyncedContentView(viewsets.ModelViewSet):
    queryset = SyncedContent.objects.all()
    serializer_class = SyncedContentSerializer
