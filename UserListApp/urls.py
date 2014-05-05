from django.conf.urls import patterns, url
from UserListApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/$', views.edit, name='edit'),
]
