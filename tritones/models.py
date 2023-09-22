from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10) # has special chars so have to use charField
    voicePart = models.CharField(max_length=30, null=True, blank=True)
    board = models.CharField(max_length=50, null=True, blank=True)
    classLevel = models.CharField(max_length=30, null=True, blank=True)
    funFacts = models.CharField(max_length=1000, null=True, blank=True)
    hometown = models.CharField(max_length=50, null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    imageUrl = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Photo(models.Model): 
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    event = models.CharField(max_length=100, null=True, blank=True)
    altText = models.CharField(max_length=1000, null=True, blank=True)
    imageUrl = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class TritoneSpotifyTrack(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_year = models.IntegerField()
    image_url = models.CharField(max_length=255)
    spotify_url = models.URLField()
    spotify_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
