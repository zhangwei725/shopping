from django.conf.urls import url, include
from django.contrib import admin

from apps.main import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', views.index),
    url('shop/', include('detail.urls')),
    url('search/', include('search.urls'))
]
