from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^agenda/$', views.agenda, name='agenda'),
    url(r'^comite/$', views.comite, name='comite'),
    url(r'^conferencistas/$', views.conferencistas, name='conferencistas'),
    url(r'^entidades/$', views.entidades, name='entidades'),
    url(r'^preregistro/$', views.preregistro, name='preregistro'),	
    url(r'^venue/$', views.venue, name='venue'),	
]
