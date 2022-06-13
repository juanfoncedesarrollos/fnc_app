from ast import Return
from django.shortcuts import render
from .serializers import *
from .models import *

from django import shortcuts
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class PersonaView(APIView):

    def post(self, request):
        try:
            person_serializer = PersonSerializer(data=request.data)
            if(person_serializer.is_valid()):
                person_serializer.save()
                return Response(PersonSerializer(person_serializer).data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(str(error), status=status.HTTP_503_SERVICE_UNAVAILABLE)

class TypeDocumentView(APIView):
    
    def get(self, request):
        try:
            type_document = TypeDocument.objects.all()
            serializer = TypeDocumentSerializer(type_document, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(str(error), status=status.HTTP_503_SERVICE_UNAVAILABLE)

# Create your views here.
