from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from .views import *


urlpatterns = [
    url(r'^$', index),
    url(r'^about/$', about),
    url(r'^team/$', team),
    ]