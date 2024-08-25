# Delete Operation

To delete the book with the title "Nineteen Eighty-Four" and confirm the deletion, use the following commands in the Django shell:

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
remaining_books = Book.objects.all()
print(remaining_books)