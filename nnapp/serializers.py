from rest_framework import serializers
from .models import UploadedData, NeuralNetwork, Result
from django.contrib.auth.models import User

 
class UploadedDataSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UploadedData
        fields = ['data_file', 'uploaded_by']

class NeuralNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeuralNetwork
        fields = ['model_name', 'description']


class ResultSerializer(serializers.Serializer):
    class Meta:
        model = NeuralNetwork
        fields = ['__all__']