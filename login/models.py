from django.db import models
from django.contrib.auth.models import  User
# Create your models here.


class PlayList(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ',' + self.creator.username

    def save(self, *args, **kwargs):
        self.title = str(self.title).replace(' ','_')
        super().save(*args, **kwargs)

class Requests(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=3000)

    def __str__(self):
        return  self.creator.username