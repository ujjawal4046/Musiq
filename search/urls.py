from django.conf.urls import url,include
from . import views
from login.views import login_user,register,top_playlist

urlpatterns = [
    url(r'artist/(?P<title>[a-zA-Z0-9 ]+)',views.artist_detail,name='artist_detail'),
    url(r'album/(?P<title>[a-zA-Z0-9 ]+)',views.album_detail,name='album_detail'),
    url(r'new_songs',views.new_songs,name='new_songs'),
    url(r'top_charts',views.top_chart_details,name='top_charts'),

    url(r'^', views.search, name='index'),

]
