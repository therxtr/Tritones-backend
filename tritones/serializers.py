from rest_framework import serializers
from .models import exampleModel

class exampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = exampleModel
        fields = ('name', 'lastname')