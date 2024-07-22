from rest_framework import serializers
from .models import UploadedData, NeuralNetwork, Result
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UploadedDataSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UploadedData
        fields = ['data_file', 'uploaded_by']

class NeuralNetworkSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = NeuralNetwork
        fields = ['model_name', 'description', 'model_file', 'uploaded_by']


class ResultSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Result
        fields = '__all__'
        # fields = ['uploaded_data', 'neural_network_model', 'result_values', 'uploaded_by']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

