"""
.. Copyright 2012 Cantemo AB. All Rights Reserved
"""

from django.conf.urls import url
from .views import GoogleAnalyticsView
# We only have one url in this app
urlpatterns = [
    url(r'^settings/$', GoogleAnalyticsView, kwargs={'template': 'analytics/settings.html'}, name='analytics_settings'),
]
