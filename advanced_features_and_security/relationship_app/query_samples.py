from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

if __name__ == "__main__":
    author_books = books_by_author('George Orwell')
    for book in author_books:
        print(book.title)

    library_books = books_in_library('Central Library')
    for book in library_books:
        print(book.title)

    librarian = librarian_of_library('Central Library')
    print(librarian.name)
