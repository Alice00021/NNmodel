from rest_framework import generics
from .models import UploadedData, NeuralNetwork, Result
from .serializers import UploadedDataSerializer, NeuralNetworkSerializer, ResultSerializer
from rest_framework import  viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from .permissions import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_protect
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#####################UploadedData###################################################
class UploadedDataAPIList(generics.ListCreateAPIView):
    queryset = UploadedData.objects.all()
    serializer_class = UploadedDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @staticmethod
    def upload_form_view(request):
        return render(request, 'upload_form.html')

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
    [permissions.IsAuthenticated, IsOwnerOrReadOnly]

#############################################################################################

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Разрешаем доступ без аутентификации

    def perform_create(self, serializer):
        serializer.save()

    @staticmethod
    @csrf_protect
    def register_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            
            if password == confirm_password:
                # Создаем пользователя
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login/')  # Редирект на страницу логина или другую страницу
            else:
                messages.error(request, 'Passwords do not match.')
        
        # Если метод GET или произошла ошибка, отображаем форму регистрации
        return render(request, 'register.html')
    
    @staticmethod
    def obtain_token_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                token_pair = TokenObtainPairView().post(request)
                return Response(token_pair.data)
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
        
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
    """ @staticmethod
    def logout_view(request):
        logout(request)
        return redirect('api-v1-datalist')   """
    
