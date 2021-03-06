"""musiq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from musiq.views import index
from django.conf import settings
from django.conf.urls.static import static
from login.views import register,login_user,logout_user,home_user,top_playlist,requests,add_playlist
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^index/$',index),
    url(r'^register',register),
    url(r'^search',include('search.urls')),
    url(r'^login',login_user),
    url(r'^logout',logout_user),
    url(r'top_playlist',top_playlist,name='top_playlist'),
    url(r'^home_user',home_user),
    url(r'^requests',requests),
    url(r'^add_playlist/(?P<title>[a-zA-Z0-9_]+)',add_playlist)

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
