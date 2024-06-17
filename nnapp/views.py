from rest_framework import generics
from .models import UploadedData, NeuralNetwork, Result
from .serializers import UploadedDataSerializer, NeuralNetworkSerializer, ResultSerializer
from rest_framework import  viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from .permissions import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#####################UploadedData###################################################
class UploadedDataAPIList(generics.ListCreateAPIView):
    queryset = UploadedData.objects.all()
    serializer_class = UploadedDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UploadedDataAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = UploadedData.objects.all()
    serializer_class = UploadedDataSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class UploadedDataAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UploadedData.objects.all()
    serializer_class = UploadedDataSerializer
    permission_classes = [IsOwnerOrReadOnly]

#####################NeuralNetwork###################################################
class NeuralNetworkAPIList(generics.ListCreateAPIView):
    queryset = NeuralNetwork.objects.all()
    serializer_class = NeuralNetworkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class NeuralNetworkAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = NeuralNetwork.objects.all()
    serializer_class = NeuralNetworkSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class NeuralNetworkAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = NeuralNetwork.objects.all()
    serializer_class = NeuralNetworkSerializer
    permission_classes = [IsOwnerOrReadOnly]
#####################Result###################################################
class ResultAPIList(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ResultAPIListDestroy(generics.RetrieveDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

#############################################################################################

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Разрешаем доступ без аутентификации

    def perform_create(self, serializer):
        serializer.save()

