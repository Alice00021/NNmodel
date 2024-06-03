# Импорт модуля admin из библиотеки Django.contrib
from django.contrib import admin

# Импорт моделей из текущего каталога (".")
from .models import UploadedData
from .models import NeuralNetworkModel
from .models import Result

# Регистрация моделей для административного сайта
admin.site.register(UploadedData)
admin.site.register(NeuralNetworkModel)
admin.site.register(Result)
