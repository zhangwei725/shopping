from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from apps.main import views
import xadmin

urlpatterns = [
                  url(r'^ueditor/', include('DjangoUeditor.urls')),
                  url('xadmin/', xadmin.site.urls),
                  url('^$', views.index),
                  url('shop/', include('detail.urls')),
                  url('search/', include('search.urls')),
                  url('account/', include('account.urls')),
                  url('cart/', include('cart.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
