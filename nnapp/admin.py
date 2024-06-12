# Импорт модуля admin из библиотеки Django.contrib
from django.contrib import admin

# Импорт моделей из текущего каталога (".")
from .models import UploadedData
from .models import NeuralNetwork
from .models import Result

# Регистрация моделей для административного сайта
admin.site.register(UploadedData)
admin.site.register(NeuralNetwork)
admin.site.register(Result)
