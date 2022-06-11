from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *
from django.conf import settings
import requests 

class BikeTypeSerializer(serializers.Serializer):
    
    description_type = serializers.CharField(required=True)
    
    class Meta:
        model = BikeType
        fields = '__all__'

    def create(self, validated_data):
        return BikeType.objects.create(**validated_data)
    
