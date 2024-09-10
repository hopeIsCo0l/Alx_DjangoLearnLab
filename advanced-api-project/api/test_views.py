from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author
from .serializers import BookSerializer

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create test data
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')  # Use login for authentication
        
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2023,
            author=self.author
        )
        self.book_data = {
            'title': 'Updated Test Book',
            'publication_year': 2024,
            'author': self.author.id
        }

    def test_create_book(self):
        response = self.client.post('/api/books/create/', {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        response = self.client.put(f'/api/books/{self.book.id}/update/', self.book_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, self.book_data['title'])

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get('/api/books/?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        response = self.client.get('/api/books/?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_ordering_books(self):
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['results'][0]['publication_year'] <= response.data['results'][1]['publication_year'])

    def test_permission(self):
        self.client.logout()
        response = self.client.post('/api/books/create/', {
            'title': 'Another Book',
            'publication_year': 2024,
            'author': self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
