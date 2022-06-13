#from typing_extensions import Required
from rest_framework import serializers
from .models import *

class TypeDocumentSerializer(serializers.Serializer):
    description_type = serializers.CharField(required=True)

    class meta:
        model = TypeDocument
        fields = '__all__'

    def create(self, validated_data):
        return TypeDocument.objects.create(**validated_data)


class PersonSerializer(serializers.Serializer):
    type_document = serializers.IntegerField(required=True)
    document_number = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    addres = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)