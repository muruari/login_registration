from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/$', views.users),
    url(r'^create_user$', views.create_user),
    url(r'^restful_users/show/(?P<id>\d+)$', views.show),  # This line has changed!
    url(r'^users/new$', views.new),
    url(r'^users/edit/(?P<id>\d+)$', views.edit),
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^users/(?P<id>\d+)/process_edit$', views.process_edit),
#  url(r'^create$', views.create),
#  url(r'^[0-9]$', views.show),     # This line has changed!
#  url(r'^[0-9]/edit$', views.edit),     # This line has changed!
#  url(r'^[0-9]/delete$', views.destroy)     # This line has changed!
]

#/{{number}}/delete