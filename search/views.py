from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime

from .models import Album,Track,Genre,Artist,Top_Chart,Chart_member
from login.models import PlayList
filter_map = {'track':Track,'album':Album,'genre':Genre,'artist':Artist,'playlist':PlayList}

def search(request):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
    if request.method == 'GET':
        searchid = request.GET.get('search_query')
        if (request.GET.get('mybtn')):
            try:
                rate = abs(int(request.GET.get('rating'))) % 100
                playlist_name = request.GET.get('playlist_name')
                playlist = PlayList.objects.get(title=playlist_name)
                playlist.rating = (playlist.rating * playlist.rating_count + rate) / (playlist.rating_count + 1)
                playlist.rating_count += 1
                playlist.save()
            except ValueError:
                pass
            return redirect('/')
        if (request.GET.get('tbutton')):
            try:
                rate = abs(int(request.GET.get('rating'))) % 100
                track_name = request.GET.get('track_name')
                track = Track.objects.get(title=track_name)
                track.rating = (track.rating * track.rating_count + rate) / (track.rating_count + 1)
                track.rating_count += 1
                track.save()
            except ValueError:
                pass
            return redirect('/')
        if not searchid:
            return redirect('/')
        filter = str(request.GET.get('filter')).lower()
        result = filter_map[filter].objects.filter(title__icontains=searchid).order_by('title')

        if filter == 'track':
            return render(request,'track_result.html',{'Track':result,'query':searchid,'authentic':authentic})
        elif filter == 'artist':
            return render(request,'artist_result.html',{'Artist':result,'query':searchid,'authentic':authentic})
        elif filter == 'album':
            return render(request, 'album_result.html', {'Album':result,'query':searchid,'authentic':authentic})
        elif filter == 'playlist':
            tracks = {}
            for r in result:
                tracks[r.title] = r.track_set.all()
                name = request.user.username
            return render(request,'top_playlist.html',{'playlist':result,'authentic':authentic,'tracks':tracks})
        else:
            return render(request,'genre_result.html',{'Genre':result,'query':searchid,'authentic':authentic})
    else:
        return render(request, 'index.html')

def artist_detail(request,title):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
    result = Artist.objects.get(title=title)
    tracks = result.track_set.all()
    return render(request,'artist_details.html',{'artist':result,'tracks':tracks,'authentic':authentic})

def genre_details(request,genre):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
    result = Genre.objects.get(title=genre)
    return render(request,'genre_details.html',{'genre_details':result,'authentic':authentic})

def top_chart_details(request):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
    result = Top_Chart.objects.all()
    track = {}
    for r in result:
        track[r.title] = r.track_set.all()
    return render(request,'top_charts.html',{'top_chart':result,'tracks':track,'authentic':authentic})

def album_detail(request,title):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
        if (request.GET.get('mybtn')):
            try:
                rate = abs(int(request.GET.get('rating')))%100
                album = Album.objects.get(title=title)
                album.rating = (album.rating*album.rating_count+rate)/(album.rating_count+1)
                album.rating_count += 1
                album.save()
            except ValueError:
                pass
            return redirect('/')
    result = Album.objects.get(title=title)
    tracks = result.track_set.all()
    return render(request, 'album_details.html', {'album': result, 'tracks': tracks,'authentic':authentic})
def top_rated_complete(request):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
    track_result = Track.objects.all().order_by('-rating')[:20]
    album_result = Album.objects.all().order_by('-rating')[:20]
    results = {'track_result':track_result,'album_result':album_result,'authentic':authentic}
    return render(request,'top_rated_complete.html',results)

##complete this
def new_songs(request):
    authentic = False
    if request.user.is_authenticated:
        authentic = True
        if (request.GET.get('tbutton')):
            try:
                rate = abs(int(request.GET.get('rating'))) % 100
                track_name = request.GET.get('track_name')
                track = Track.objects.get(title=track_name)
                track.rating = (track.rating * track.rating_count + rate) / (track.rating_count + 1)
                track.rating_count += 1
                track.save()
            except ValueError:
                pass
            return redirect('/')
    now = datetime.datetime.now()
    result = Track.objects.filter(year=now.year).order_by('title')
    return render(request, 'track_result.html', {'Track': result, 'query': 'New Songs','authentic':authentic})
