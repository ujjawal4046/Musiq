from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import  UserForm
from .models import PlayList,Requests
from search.models import Track
# Create your views here.
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        'authentic':False
    }
    return render(request, 'index.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            authentic = False
            if user.is_active:
                login(request, user)
                authentic = True
                playlist = None
                return redirect('/')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


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
            authentic = False
            if user.is_active:
                authentic = True
                login(request, user)

                return redirect('/')
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

def home_user(request):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
        if request.method == 'GET':
            title = request.GET.get('title')
            check = PlayList.objects.filter(creator=request.user,title=title).order_by('title')
            p = PlayList()
            p.title = title
            p.rating  = 0
            p.creator = request.user
            if title and not check:
                p.save()
        playList = PlayList.objects.filter(creator=request.user).order_by('title')
        tracks =  {}
        for r in playList:
            tracks[r.title] = r.track_set.all()
        name = request.user.username
        return render(request,'home_user.html',{'authentic':authentic,'name':name,'playlist':playList,'tracks':tracks})
    else:
        return redirect('/')

def top_playlist(request):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
    if (request.GET.get('mybtn')):
        try:
            rate = abs(int(request.GET.get('rating'))) % 100
            playlist_name = request.GET.get('playlist_name')
            print(playlist_name)
            playlist = PlayList.objects.get(title=playlist_name)
            playlist.rating = (playlist.rating * playlist.rating_count + rate) / (playlist.rating_count + 1)
            playlist.rating_count += 1
            playlist.save()
        except ValueError:
            pass
        return redirect('/')
    playlist = PlayList.objects.filter(rating__gte=90).order_by('rating')
    tracks = {}
    for r in playlist:
        tracks[r.title] = r.track_set.all()
        name = request.user.username
    return render(request, 'top_playlist.html',{'authentic': authentic, 'playlist': playlist, 'tracks': tracks})

def requests(request):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
        if request.method =="POST":
            des = request.POST.get('request')
            new_request = Requests()
            new_request.creator = request.user
            new_request.description = des
            new_request.save()
            return redirect('/')
        return render(request,'request.html',{'authentic':authentic})
    else:
        return redirect('/login')

def add_playlist(request,title):
    if request.user.is_authenticated:
        authentic = True
        if request.method == "POST":
            playlist_name = request.POST.get('playlist_title')
            req_play = PlayList.objects.get(title=playlist_name)
            req_play.track_set.add(Track.objects.get(title=title))
            req_play.save()
            return redirect('/home_user')
        playlists = PlayList.objects.filter(creator=request.user)
        return render(request,'add_playlist.html',{'playlist':playlists,'authentic':authentic})

    else:
        return redirect('/')