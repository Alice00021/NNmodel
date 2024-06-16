from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UploadedData(models.Model):
    data_file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User,  on_delete=models.CASCADE)

class NeuralNetwork(models.Model):
    model_name = models.CharField(max_length=100)
    description = models.TextField()
    model_file = models.FileField(upload_to='models/')
    upload_date = models.DateTimeField(auto_now_add=True)

class Result(models.Model):
    uploaded_data = models.ForeignKey(UploadedData, on_delete=models.CASCADE)
    neural_network_model = models.ForeignKey(NeuralNetwork, on_delete=models.CASCADE)
    result_values = models.TextField()



  
