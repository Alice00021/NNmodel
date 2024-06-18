from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

class UserCreateAPITestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.user_data = {
            'username': 'testuser',
            'password': 'password123',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)  # Проверяем, что пользователь был создан
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_user_registration_missing_fields(self):

        incomplete_data = {
            'password': 'password456',
            'email': 'testuser2@example.com'
        }
        response = self.client.post(self.register_url, incomplete_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Тест на регистрацию с уже существующим именем пользователя
    def test_user_registration_existing_username(self):
        User.objects.create_user(**self.user_data)  
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)