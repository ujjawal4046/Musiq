from django.shortcuts import render
from django.http import HttpResponse
from .models import Album,Track,Genre,Artist
filter_map = {'track':Track,'album':Album,'genre':Genre,'artist':Artist}

def search(request):
    if request.method == 'GET':
        searchid = request.GET.get('search_query')
        filter = str(request.GET.get('filter')).lower()
        result = filter_map[filter].objects.filter(title__icontains=searchid)

        if filter == 'track':
            return render(request,'track_results.html',{'Track':result})
        elif filter == 'artist':
            return render(request,'artist_result.html',{'Artist':result})
        elif filter == 'album':
            return render(request, 'artist_result.html', {'Album':result})
        else:
            return render(request,'genre_result.html',{'Genre':result})
    else:
        return render(request, 'index.html')

def artist_detail(request,title):
    artist = Artist.objects.get(title=title)
    return render(request,'details.html')