from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm


@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    # Logic to add a new book
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to edit the book
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to delete the book
    return render(request, 'relationship_app/delete_book.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/books.html', {'books': books})

#Example view in views.py
def example_view(request):
    form = ExampleForm()
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle form processing
            pass
    return render(request, 'bookshelf/form_example.html', {'form': form})




