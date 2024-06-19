from urllib.parse import urlparse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from ..models import NeuralNetwork
from django.core.files.uploadedfile import SimpleUploadedFile

class UploadedDataAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = RefreshToken.for_user(self.user)
        self.access_token = str(self.token.access_token)
        self.api_authentication()

        self.uploaded_data = NeuralNetwork.objects.create(model_name='model3', description='create new model - model3', model_file='test.txt', uploaded_by=self.user)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {self.access_token}')

    def test_list_uploaded_data(self):
        url = reverse('api-v1-model')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_uploaded_data(self):
        url = reverse('api-v1-modelupdate', kwargs={'pk': self.uploaded_data.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        parsed_url = urlparse(response.data['model_file'])
        filename = parsed_url.path.split('/')[-1]  # Получаем последний сегмент пути (имя файла)
        self.assertEqual(filename, 'test.txt')

    
    def test_update_uploaded_data(self):
        url = reverse('api-v1-modelupdate', kwargs={'pk': self.uploaded_data.pk})
        file_content = b'Test file content 2'  # Замените на содержимое вашего файла
        uploaded_file = SimpleUploadedFile('updated_test1.txt', file_content)
        data = {'data_file': uploaded_file}
        
        response = self.client.put(url, data, format='multipart')
        
        print(response.status_code)  # Печатаем код состояния HTTP
        print(response.data)  # Печатаем данные, возвращаемые в ответе
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.uploaded_data.refresh_from_db()
        parsed_url = urlparse(response.data['data_file'])
        filename = parsed_url.path.split('/')[-1]
        print(parsed_url)
        print(filename)
        print(self.uploaded_data.data_file)
        self.assertTrue(filename.startswith('updated_test1_') and filename.endswith('.txt'))
    """ def test_delete_uploaded_data(self):
        url = reverse('api-v1-modeldelete', kwargs={'pk': self.uploaded_data.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(NeuralNetwork.objects.filter(pk=self.uploaded_data.pk).exists())
 """
    """ def test_unauthorized_access(self):
        self.client.credentials() 
        url = reverse('api-v1-datalist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permission_owner_update(self):
        # Проверяем, что только владелец может обновить данные
        other_user = User.objects.create_user(username='otheruser', password='password456')
        token = RefreshToken.for_user(other_user)
        access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {access_token}')
        url = reverse('api-v1-dataupdate', kwargs={'pk': self.uploaded_data.pk})
        data = {'data_file': 'updated_by_other.txt'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_permission_owner_delete(self):
        # Проверяем, что только владелец может удалить данные
        other_user = User.objects.create_user(username='otheruser', password='password456')
        token = RefreshToken.for_user(other_user)
        access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {access_token}')
        url = reverse('api-v1-datadestroy', kwargs={'pk': self.uploaded_data.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) """