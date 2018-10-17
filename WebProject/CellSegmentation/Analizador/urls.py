from django.conf.urls import url
from . import views

app_name = 'analizador'

urlpatterns = [
    url(r'^list/$', views.list_collections, name="list"),
    url(r'^predictions/(?P<value>\d+)/$', views.predict_collection, name='predict_collection'),
]