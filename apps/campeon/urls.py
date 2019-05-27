from django.conf.urls import url
from rest_framework import routers
from apps.campeon.views import *

urlpatterns = [
    url(r'^campeon/$', CampeonList.as_view(),name='campeonList'),
    url(r'^campeon/(?P<pk>\d+)/?$', CampeonList.as_view())
]