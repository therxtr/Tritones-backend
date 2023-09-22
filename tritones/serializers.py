from rest_framework import serializers
from .models import Member, TritoneSpotifyTrack, Photo


class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'number', 'voicePart', 'board', 'classLevel', 'hometown', 'funFacts', 'major', 'imageUrl')

class photoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Photo
        fields = ('name', 'year', 'event', 'altText', 'imageUrl')

class tritoneSpotifyTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TritoneSpotifyTrack
        fields = ('name', 'artist', 'album', 'release_year', 'image_url', 'spotify_url', 'spotify_id')

