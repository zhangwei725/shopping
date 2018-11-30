from django.conf.urls import url

from apps.cart import views

urlpatterns = [
    url('add/', views.add_car, name='add'),
    url('list/', views.list, name='list'),
    url('confirm/', views.confirm, name='confirm'),
    url(r'order/', views.confirm1, name='order')
]
