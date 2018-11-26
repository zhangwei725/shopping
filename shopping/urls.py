from django.conf.urls import url
from django.contrib import admin

from apps.main import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', views.index),
]
