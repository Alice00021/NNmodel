from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from nnapp.views import *

router = routers.SimpleRouter()
router.register(r'datalist', UploadedDataViewSet)
router.register(r'model', NeuralNetworkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls)),
]

