from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from nnapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/datalist/',UploadedDataAPIList.as_view()),
    path('api/v1/datalist/<int:pk>/',UploadedDataAPIUpdate.as_view()),
    path('api/v1/datalistdelete/<int:pk>/',UploadedDataAPIDestroy.as_view()),
    
    path('api/v1/model/',NeuralNetworkAPIList.as_view()),
    path('api/v1/model/<int:pk>/',NeuralNetworkAPIUpdate.as_view()),
    path('api/v1/modeldelete/<int:pk>/',NeuralNetworkAPIDestroy.as_view()),

    path('api/v1/result/',ResultAPIListDestroy.as_view()),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', UserCreate.as_view(), name='register'),
]

