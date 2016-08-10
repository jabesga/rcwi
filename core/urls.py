from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^update-ip/$', views.manual_update_ip, name="manual_update_ip"),
                       url(r'^open-gate/$', views.open_gate, name="open_gate"),
                       url(r'^logs/$', views.logs, name="logs"),
                       url(r'^card/(?P<card_id>\d{1,3})/$', views.card, name="card"),
                       url(r'^owner/(?P<owner_id>\d{1,3})/$', views.owner, name="owner"),
                       url(r'^owner/add/$', views.add_owner, name="add_owner"),
                       url(r'^ariz/puerta/subir/$', views.up_door, name="up_door"),
                       url(r'^ariz/puerta/bajar/$', views.down_door, name="down_door"),
                       )


