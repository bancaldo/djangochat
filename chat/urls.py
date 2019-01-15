# noinspection PyUnresolvedReferences
from django.contrib import admin
# noinspection PyUnresolvedReferences
from django.conf.urls import include, url
# noinspection PyUnresolvedReferences
from chat import views

urlpatterns = [
    url(r'^chat$', views.chat, name='chat'),
]
