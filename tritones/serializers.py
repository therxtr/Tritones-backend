from rest_framework import serializers
from .models import Member, TritoneSpotifyTrack


class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'number', 'voicePart')

class tritoneSpotifyTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TritoneSpotifyTrack
        fields = ('name', 'artist', 'album', 'release_year', 'image_url', 'spotify_url', 'spotify_id')

