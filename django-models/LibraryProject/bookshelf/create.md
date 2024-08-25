# Create Operation

To create a new `Book` instance with the title "1984", author "George Orwell", and publication year 1949, use the following commands in the Django shell:

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()