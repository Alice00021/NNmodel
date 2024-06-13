from django.contrib import admin
from django.urls import path

from nnapp.views import DataAPIView
from nnapp.views import NeuralNetworkAPIView
""" from nnapp.views import uploaded_data_list
from rest_framework.urlpatterns import format_suffix_patterns """

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/datalist/', DataAPIView.as_view()),
    path('api/v1/model/', NeuralNetworkAPIView.as_view()),
    path('api/v1/datalist/<int:pk>/',DataAPIView.as_view())
    #path('uploadeddata/', uploaded_data_list),
]

""" urlpatterns = format_suffix_patterns(urlpatterns) """
