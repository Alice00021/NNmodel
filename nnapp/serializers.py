from rest_framework import serializers
from .models import UploadedData, NeuralNetwork, Result
from django.contrib.auth.models import User

class UploadedDataSerializer(serializers.Serializer):
    data_file = serializers.FileField()
    upload_date = serializers.DateTimeField(read_only=True)
    uploaded_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    def create(self, validated_data):
        return UploadedData.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.data_file = validated_data.get("data_file", instance.data_file)
        instance.upload_date = validated_data.get("upload_date", instance.upload_date)
        instance.uploaded_by = validated_data.get("uploaded_by", instance.uploaded_by)
        instance.save()
        return instance

class NeuralNetworkSerializer(serializers.Serializer):
    model_name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    model_file = serializers.FileField(read_only=True)
    upload_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return NeuralNetwork.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.model_name = validated_data.get("model_name", instance.model_name)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance
    


""" class ResultSerializer(serializers.Serializer):
    uploaded_data = serializers.PrimaryKeyRelatedField(queryset=UploadedData.objects.all())
    neural_network_model = serializers.PrimaryKeyRelatedField(queryset=NeuralNetwork.objects.all())
    result_values = serializers.CharField() """