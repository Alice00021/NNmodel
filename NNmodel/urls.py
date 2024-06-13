from django.contrib import admin
from django.urls import path

from nnapp.views import DataAPIView
from nnapp.views import NeuralNetworkAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/datalist/', DataAPIView.as_view()),
    path('api/v1/datalist/<int:pk>/',DataAPIView.as_view()),
    path('api/v1/model/', NeuralNetworkAPIView.as_view()),
    path('api/v1/model/<int:pk>/', NeuralNetworkAPIView.as_view()),

]

