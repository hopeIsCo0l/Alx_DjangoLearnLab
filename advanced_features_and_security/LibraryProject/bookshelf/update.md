# Update Operation

To update the title of the book from "1984" to "Nineteen Eighty-Four", use the following command in the Django shell:

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)