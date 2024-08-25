from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import list_books

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Admin, Librarian, and Member views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Book-related views
    path('books/', views.list_books, name='list_books'),  # List books
    path('books/add/', views.add_book, name='add_book/'),  # Add a book
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book/'),  # Edit a book
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),  # Delete a book

    # Library detail view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Include the app's URLs
]