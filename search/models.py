from django.db import models
from django.conf import settings
import urllib
from bs4 import BeautifulSoup

def search_youtube(name):
    query = urllib.parse.quote(name)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    links = soup.findAll(attrs={'class': 'yt-uix-tile-link'})
    if links:
        return(str('https://www.youtube.com' + links[0]['href']))


class Genre(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    popular_artists = models.CharField(max_length=100)
    popular_tracks = models.CharField(max_length=100)
    genre_logo = models.FileField(null=True,blank=True)
    def __str__(self):
        return self.title
    class Admin:pass

class Album(models.Model):
    title = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    length = models.TimeField(default='0:00:00')
    year = models.IntegerField(null=True)
    rating = models.IntegerField(null=True,blank=True,default=0)
    album_logo = models.FileField(null=True,blank=True)
    def __str__(self):
        return self.title
    class Admin:pass


class Artist(models.Model):
    title = models.CharField(max_length=50)
    country = models.CharField(max_length=25)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=1000,blank=True)
    artist_logo = models.FileField(null=True,blank=True)

    ## awards and tracks

    def __str__(self):
        return self.title
    class Admin:
        list_display = ('title','year','country')
        list_filter = ('country','year')
        ordering = ('title')
        search_fields = ('title')

class Top_Chart(models.Model):
    title = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    description = models.TextField(null=True,blank=True)

    class Admin: pass

class Track(models.Model):
    title = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    year = models.IntegerField(null=True)
    country = models.CharField(max_length=25,blank=True, null=True)
    language = models.CharField(max_length=25)
    length = models.TimeField(default='0:00:00')
    rating = models.IntegerField(null=True,blank=True,default=0)
    charts = models.ManyToManyField(Top_Chart,through='Chart_member',null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    def __str__(self):
        return self.title

    class Admin: pass

    def save(self, *args, **kwargs):
        if self.country is None:
            self.country = self.artist.country
        if self.url is None:
            link = search_youtube(self.title + " " + str(self.artist.title))
            self.url = link
        super().save(*args, **kwargs)

class Chart_member(models.Model):
    track = models.ForeignKey(Track,on_delete=models.CASCADE)
    top_chart = models.ForeignKey(Top_Chart,on_delete=models.CASCADE)
    rank = models.SmallIntegerField()
    weeks = models.IntegerField()

    class Admin: pass














