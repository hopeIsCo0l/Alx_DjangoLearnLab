from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),               # List all books and create new book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),   # Retrieve a book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),     # Create a new book (without pk in URL)
    path('books/update/', BookUpdateView.as_view(), name='book-update'),     # Update a book (without pk in URL)
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),     # Delete a book (without pk in URL)
]
