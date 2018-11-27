from django.conf.urls import url

from apps.detail import views

"""
url('detail' shop.shop_id)'
"""
urlpatterns = [
    url('detail/', views.detail, name='detail')
]
