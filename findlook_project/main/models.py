from distutils.command.upload import upload
from hashlib import blake2b
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=156, unique=True)

    def __str__(self) -> str:
        return self.topic_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=CASCADE, related_name='webpages') 
    name = models.CharField(max_length=156, unique=True)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=CASCADE, related_name='access_records')
    date = models.DateField()

    def __str__(self) -> str:
        return str(self.date)

class UserSuggested(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=500, default='')

    def __str__(self) -> str:
        return self.email


class UserProfileInfo(models.Model):
    """ Extend the basic user class to add new fields"""
    user = models.OneToOneField(User, on_delete=CASCADE)

    # additional fields
    # instagramm_link = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self) -> str:
        return self.user.username
