from django.shortcuts import render
from rest_framework import viewsets
from sync_control.models import UserProfile
from sync_control.models import UserProfileSerializer


class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
