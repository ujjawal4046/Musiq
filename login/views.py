from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import  UserForm
from .models import PlayList,Requests
# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                playlist = PlayList.objects.filter(user=request.user)
                return render(request, 'user_view.html', {'playlist': playlist})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                playlist = PlayList.objects.filter(user=request.user)
                return render(request, 'user_view.html', {'playlist': playlist})
    context = {
        "form": form,
    }
    return render(request, 'user_register.html', context)
