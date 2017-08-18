from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.basic, name='basic'),
    url(r'^manual/$', views.manual, name='manual'),
    url(r'^field/$', views.field, name='field'),
    url(r'^attrs/$', views.attrs, name='attrs'),
    url(r'^tweaks/$', views.tweaks, name='tweaks'),
    url(r'^bootstrap4/$', views.bootstrap4, name='bootstrap4'),
    url(r'^user/$', views.user, name='user'),
]
