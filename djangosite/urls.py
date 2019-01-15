# djangosite\urls.py

from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('chat.urls')),
    url(r'^admin/', admin.site.urls),
]
