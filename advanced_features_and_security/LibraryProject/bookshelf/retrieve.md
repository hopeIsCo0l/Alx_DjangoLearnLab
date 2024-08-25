# Retrieve Operation

To retrieve and display all attributes of the book created with the title "1984", use the following command in the Django shell:

```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)