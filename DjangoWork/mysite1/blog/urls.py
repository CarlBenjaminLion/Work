# coding=utf-8
from django.conf.urls import url
from .views import archive

urlpatterns = [
    url(r'^$', archive, name='archive'),
]

