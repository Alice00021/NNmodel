from rest_framework import generics
from django.shortcuts import render
from .models import UploadedData
from .serializers import UploadedDataSerializer


from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework import status
from rest_framework.decorators import api_view


class DataAPIView(APIView):

    def get(self, request):
        queryset = UploadedData.objects.all()
        return Response({'data': UploadedDataSerializer(queryset, many =True).data})

    
    def post(self, request):
            #проверка данных 
        serializer = UploadedDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        """ post_new = UploadedData.objects.create(
            data_file = request.data['data_file'],
            uploaded_by = request.data['uploaded_by'],
        ) """
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


from .serializers import NeuralNetworkSerializer
from .models import NeuralNetwork
class NeuralNetworkAPIView(APIView):

    def get(self, request):
        queryset = NeuralNetwork.objects.all()
        return Response({'data': NeuralNetworkSerializer(queryset, many =True).data})

    
    def post(self, request):
            #проверка данных 
        serializer = NeuralNetworkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        """ post_new = NeuralNetwork.objects.create(

            model_name = request.data['model_name'],
            description = request.data['description'],
        ) """
        return Response({'post': serializer.data})



