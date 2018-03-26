from django.db import models
from django.contrib.auth.models import  User
# Create your models here.


class PlayList(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

class Requests(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=3000)