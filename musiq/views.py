from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
import datetime
# Create your views here.
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

def index(request):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
    return render(request,'index.html',{'authentic':authentic});
