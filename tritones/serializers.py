from rest_framework import serializers
from .models import Member, boardMember


class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'number', 'voicePart')

class boardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = boardMember
        fields = ('name', 'number', 'voicePart', 'board')

