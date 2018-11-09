from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'analizador'

urlpatterns = [
    url(r'^list/$', views.list_collections, name="list"),
    url(r'^predictions/(?P<value>\d+)/$', views.predict_collection, name='predict_collection'),
    url(r'^predictions/download/(?P<value>\d+)/$', views.download_files, name='download_files'),
]