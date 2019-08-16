from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.all_shows),
    url(r'^shows/new$', views.add_show),
    url(r'^shows/(?P<show_id>\d+)$', views.show_details),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<show_id>\d+)/delete$', views.delete_show),
    url(r'^shows/create_show$', views.create_show),
    url(r'^shows/(?P<show_id>\d+)/update_show$', views.update_show),
]
