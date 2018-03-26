from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from login.views import register,login_user
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
url(r'register',register,name='register'),
url(r'^$',login_user,name='login_user'),

]
