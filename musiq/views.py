from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
import datetime
# Create your views here.
from django.db.models import Q

def index(request):
    return render(request,'index.html');

