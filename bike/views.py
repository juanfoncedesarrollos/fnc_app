import requests
from .serializers import *
from .models import *

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# def index(request):
#     return HttpResponse('Hola buenas tardes')

# Create your views here
class BikeTypeView(APIView):
    # class bike type
    def post(self, request):
        try:
            type_bike_serilizer = BikeTypeSerializer(data=request.data)
            
            if type_bike_serilizer.is_valid():
                bike_type = type_bike_serilizer.save()
                return Response(BikeTypeSerializer(bike_type).data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        except Exception as error:
            return Response(str(error), status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
    def get(self, request):
        # get methot
        try:
            bike_type = BikeType.objects.all()
            serializer = BikeTypeSerializer(bike_type, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(str(error),status=status.HTTP_503_SERVICE_UNAVAILABLE)
