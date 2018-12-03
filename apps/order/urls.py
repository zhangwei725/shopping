from django.conf.urls import url

from apps.order import views

urlpatterns = [
    url('pay/', views.pay, name='pay')
]
