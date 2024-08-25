from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Library, Book, UserProfile
from .forms import BookForm

# Book-related views
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Ensure 'list_books' is a valid URL name
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Ensure 'list_books' is a valid URL name
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')  # Ensure 'list_books' is a valid URL name
    return render(request, 'relationship_app/delete_book.html', {'book': book})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Ensure 'home' is a valid URL name
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User role-based views
def is_admin(user):
    return UserProfile.objects.filter(user=user, role='Admin').exists()

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_member(user):
    return UserProfile.objects.filter(user=user, role='Member').exists()

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def is_librarian(user):
    return UserProfile.objects.filter(user=user, role='Librarian').exists()

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
