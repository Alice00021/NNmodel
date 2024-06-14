from rest_framework import generics
from django.shortcuts import render
from .models import UploadedData
from .serializers import UploadedDataSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NeuralNetworkSerializer
from .models import NeuralNetwork

from rest_framework import status

class DataAPIList(generics.ListAPIView):
    queryset = UploadedData.objects.all()
    serializer_class = UploadedDataSerializer

class DataAPIUpdate(generics.UpdateAPIView):
    queryset = UploadedData.objects.all()
    serializer_class = UploadedDataSerializer

class DataAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UploadedData.objects.all()
    serializer_class = UploadedDataSerializer
    
""" class DataAPIView(APIView):

    def get(self, request):
        queryset = UploadedData.objects.all()
        return Response({'data': UploadedDataSerializer(queryset, many =True).data})

    
    def post(self, request):
            #проверка данных 
        serializer = UploadedDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
     
        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method put not allowed"})
        
        try:
            instanse = UploadedData.objects.get(pk=pk)
        except:
            return Response({"error":"Objects does not exist"})
        
        serializer = UploadedDataSerializer(data=request.data, instance=instanse)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            instance = UploadedData.objects.get(pk=pk)
        except UploadedData.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"post": f"Deleted post with pk={pk}"}, status=status.HTTP_204_NO_CONTENT)

"""

