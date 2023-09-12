from rest_framework import serializers
from .models import Member, boardMember, contactModel



class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'number', 'voicePart')

class boardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = boardMember
        fields = ('name', 'number', 'voicePart', 'board')

class ContactSubmissionSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = contactModel
        fields = '__all__'

