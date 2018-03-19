from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    url(r'^artist/(?P<title>[[a-zA_Z]+]+)$',views.search,name='artist_detail'),
    url(r'^', views.search, name='index'),

]
