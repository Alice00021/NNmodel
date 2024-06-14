from rest_framework import generics
from django.shortcuts import render
from .models import UploadedData
from .serializers import UploadedDataSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NeuralNetworkSerializer
from .models import NeuralNetwork

from rest_framework import status, viewsets

class UploadedDataViewSet(viewsets.ModelViewSet):
    queryset = UploadedData.objects.all()
    serializer_class = UploadedDataSerializer

class NeuralNetworkViewSet(viewsets.ModelViewSet):
    queryset = NeuralNetwork.objects.all()
    serializer_class = NeuralNetworkSerializer


    


