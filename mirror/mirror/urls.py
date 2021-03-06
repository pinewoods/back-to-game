from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import url, include
from rest_framework import routers

import sync_control
from sync_control import views

router = routers.DefaultRouter()
router.register(r'user_profile', views.UserProfileView)

urlpatterns = [

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.

    url(r'^', include(router.urls)),
    url(r'^', include('sync_control.urls')),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),

    # Examples:
    # url(r'^$', 'mirror.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
