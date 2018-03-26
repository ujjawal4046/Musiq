from django.conf.urls import url,include
from . import views



urlpatterns = [
    url(r'artist/(?P<title>[a-zA-Z0-9 ]+)',views.artist_detail,name='artist_detail'),
    url(r'album/(?P<title>[a-zA-Z0-9 ]+)',views.album_detail,name='album_detail'),
    url(r'^', views.search, name='index'),

]
