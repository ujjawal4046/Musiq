from django.db import models
from django.conf import settings
class Genre(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    popular_artists = models.CharField(max_length=100)
    popular_tracks = models.CharField(max_length=100)
    genre_logo = models.FileField(null=True)
    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    year = models.IntegerField()
    rating = models.IntegerField()
    album_logo = models.FileField(null=True)
    def __str__(self):
        return self.title


class Artist(models.Model):
    title = models.CharField(max_length=50)
    country = models.CharField(max_length=25)
    year = models.IntegerField()
    description = models.CharField(max_length=1000,blank=True)
    artist_logo = models.FileField(null=True,blank=True)

    ## awards and tracks

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    year = models.IntegerField()
    country = models.CharField(max_length=25)
    language = models.CharField(max_length=25)
    length = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title


