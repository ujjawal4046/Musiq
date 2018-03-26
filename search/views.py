from django.shortcuts import render
from django.http import HttpResponse
from .models import Album,Track,Genre,Artist,Top_Chart
filter_map = {'track':Track,'album':Album,'genre':Genre,'artist':Artist}

def search(request):
    if request.method == 'GET':
        searchid = request.GET.get('search_query')
        filter = str(request.GET.get('filter')).lower()
        result = filter_map[filter].objects.filter(title__icontains=searchid)

        if filter == 'track':
            return render(request,'track_result.html',{'Track':result,'query':searchid})
        elif filter == 'artist':
            return render(request,'artist_result.html',{'Artist':result,'query':searchid})
        elif filter == 'album':
            return render(request, 'album_result.html', {'Album':result,'query':searchid})
        else:
            return render(request,'genre_result.html',{'Genre':result,'query':searchid})
    else:
        return render(request, 'index.html')

def artist_detail(request,title):
    result = Artist.objects.get(title=title)
    tracks = result.track_set.all()
    return render(request,'artist_details.html',{'artist':result,'tracks':tracks})

def genre_details(request,genre):
    result = Genre.objects.get(title=genre)
    return render(request,'genre_details.html',{'genre_details':result})

def top_chart_details(request,top_chart):
    result = Top_Chart.objects.get(title=top_chart)
    return render(request,'top_chart_details.html',{'top_chart':result})

def album_detail(request,title):
    result = Album.objects.get(title=title)
    tracks = result.track_set.all()
    return render(request, 'album_details.html', {'album': result, 'tracks': tracks})
def top_rated_complete(request):
    track_result = Track.objects.all().order_by('-rating')[:20]
    album_result = Album.objects.all().order_by('-rating')[:20]
    results = {'track_result':track_result,'album_result':album_result}
    return render(request,'top_rated_complete.html',results)

##complete this
def new_songs(request):
    result = Track.objects.all().filter()
    return (request,'new_songs.html',{'result':result})