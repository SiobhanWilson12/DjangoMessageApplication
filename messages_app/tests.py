from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Message

class MessageAPITestCase(APITestCase):
    def test_create_message_with_short_content(self):
        url = reverse('message-create')
        data = {'content': ''}  # Content too short
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('This field may not be blank.', response.data['content'])

    def test_create_message_with_long_content(self):
        url = reverse('message-create')
        data = {'content': 'A' * 101}  # Content too long
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Content is too long, must be less than 100 characters.', response.data['content'])

    def test_create_message_with_valid_content(self):
        url = reverse('message-create')
        data = {'content': 'Valid test message'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_messages(self):
        Message.objects.create(content='Test message')

        url = reverse('message-list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], 'Test message')

    def test_clear_messages(self):
       url = reverse('message-clear') 
       Message.objects.create(content='First message') 
       Message.objects.create(content='Second message') 

       response = self.client.delete(url)

       self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
       self.assertEqual(Message.objects.count(), 0)
