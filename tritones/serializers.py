from rest_framework import serializers
from .models import Member, boardMember, TritoneSpotifyTrack


class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'number', 'voicePart')

class boardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = boardMember
        fields = ('name', 'number', 'voicePart', 'board')

class tritoneSpotifyTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TritoneSpotifyTrack
        fields = ('name', 'artist', 'album', 'release_year', 'image_url', 'spotify_url', 'spotify_id')

