from django.conf.urls import url

from search import views

urlpatterns = [
    url('result/', views.search, name='search')
]
