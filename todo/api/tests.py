from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import TodoItem

class TodoAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo_item = TodoItem.objects.create(title='Test Todo', description='Test description')

    def test_get_todo_list(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_todo_detail(self):
        response = self.client.get(f'/api/todos/{self.todo_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Todo')

    def test_create_todo_item(self):
        data = {'title': 'New Todo', 'description': 'New description'}
        response = self.client.post('/api/todos/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TodoItem.objects.count(), 2)

    def test_update_todo_item(self):
        data = {'title': 'Updated Todo', 'description': 'Updated description'}
        response = self.client.put(f'/api/todos/{self.todo_item.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo_item.refresh_from_db()
        self.assertEqual(self.todo_item.title, 'Updated Todo')

    def test_delete_todo_item(self):
        response = self.client.delete(f'/api/todos/{self.todo_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TodoItem.objects.count(), 0)

