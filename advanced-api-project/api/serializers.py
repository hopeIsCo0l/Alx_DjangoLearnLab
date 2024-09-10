from rest_framework import serializers
from .models import Author, Book
import datetime

"""
BookSerializer:
- Serializes the Book model.
- Validates the publication year to ensure it is not in the future.

AuthorSerializer:
- Serializes the Author model.
- Dynamically includes a nested BookSerializer to serialize related books.
"""


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation for publication year
    def validate_publication_year(self, value):
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
